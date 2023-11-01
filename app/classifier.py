import numpy as np
import os
from keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import json
import argparse

os.chdir(os.path.dirname(os.path.abspath(__file__)))

parser = argparse.ArgumentParser(description="Process a photo.")
parser.add_argument("photo_path", help="Path to the input photo")
args = parser.parse_args()
photo_path = args.photo_path

class_indices_file_path = 'class_indices.json'

model = load_model('BirdModel.h5'.format(1))
with open(class_indices_file_path, 'r') as json_file:
    class_indices = json.load(json_file)

image = load_img(photo_path, target_size=(224, 224))
image = img_to_array(image)
image = np.expand_dims(image, axis=0)
image = image / 255.0

threshold = 0.8

predictions = model.predict(image)

if np.max(predictions) >= threshold:
    predicted_class_index = np.argmax(predictions)
    predicted_class_label = [k for k, v in class_indices.items() if v == predicted_class_index][0]
    print("Predicted Class Label:", predicted_class_label)
else:
    print("None of the classifiers is high enough.")


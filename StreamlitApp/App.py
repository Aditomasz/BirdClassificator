import streamlit as st
import os
import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import json

# Set the working directory to the root folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class_indices_file_path = '../model/class_indices.json'

# Load the pre-trained model and class indices
model = load_model('../model/BirdModel.h5')
with open(class_indices_file_path, 'r') as json_file:
    class_indices = json.load(json_file)

def predict_image(photo_path):
    image = load_img(photo_path, target_size=(224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image / 255.0

    predictions = model.predict(image)

    threshold = 0.8
    if np.max(predictions) >= threshold:
        predicted_class_index = np.argmax(predictions)
        predicted_class_label = [k for k, v in class_indices.items() if v == predicted_class_index][0]
        return predicted_class_label
    else:
        return "None of the classifiers is high enough."

def main():
    st.title("Photo Prediction App")

    uploaded_file = st.file_uploader("Choose a photo...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Make predictions when the user clicks the button
        if st.button("Predict"):
            # Save the uploaded file to a temporary location
            temp_path = "temp_image.png"
            with open(temp_path, "wb") as temp_file:
                temp_file.write(uploaded_file.getvalue())

            # Call the prediction function
            prediction_result = predict_image(temp_path)
            st.write("Prediction Result:", prediction_result)

            # Remove the temporary file
            os.remove(temp_path)

if __name__ == "__main__":
    main()
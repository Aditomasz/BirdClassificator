import os
import pandas as pd
import json
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from dotenv import load_dotenv

load_dotenv()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

data_dir = os.getenv("DATA_DIR")
csv_path = os.getenv("CSV_PATH")
class_indices_file_path = 'class_indices.json'

train_dir = os.path.join(data_dir, "train")
test_dir = os.path.join(data_dir, "test")
valid_dir = os.path.join(data_dir, "valid")

contents = os.listdir(train_dir)
folders = [item for item in contents if os.path.isdir(os.path.join(train_dir, item))]
num_folders = len(folders)

print(f"Number of folders in the directory: {num_folders}")


df = pd.read_csv(csv_path)

datagen = ImageDataGenerator(
    rescale=1.0/255.0,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    zoom_range=0.2 
)

train_generator = datagen.flow_from_directory(
    train_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical' 
)

test_generator = datagen.flow_from_directory(
    test_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)

valid_generator = datagen.flow_from_directory(
    valid_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)

class_indices = train_generator.class_indices
with open(class_indices_file_path, 'w') as json_file:
    json.dump(class_indices, json_file)

filepaths = df['filepaths'].values
labels = df['labels'].values

model = Sequential()
model.add(Conv2D(64, (3, 3), activation='relu', input_shape=(224, 224, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(256, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(num_folders*8, activation='relu'))
model.add(Dense(num_folders*4, activation='relu'))
model.add(Dense(num_folders, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model.fit(
    train_generator,
    epochs=15,
    validation_data=valid_generator 
)

test_loss, test_accuracy = model.evaluate(test_generator)
print(f'Test accuracy: {test_accuracy}')

model.save('BirdModel.h5'.format(1))
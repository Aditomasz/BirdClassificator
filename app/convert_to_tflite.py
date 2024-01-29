import tensorflow as tf
from keras.models import load_model

# Zapisz model w formacie SavedModel
model = load_model('BirdModel.h5'.format(1))
model.save('saved_model', save_format='tf')

# Wczytaj model SavedModel
saved_model_path = 'saved_model'
model = tf.saved_model.load(saved_model_path)

print("Model TensorFlow pomyślnie załadowany.")

# Konwertuj model na format TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_path)
tflite_model = converter.convert()

# Zapisz model TensorFlow Lite do pliku
output_tflite_path = 'model.tflite'
with open(output_tflite_path, 'wb') as f:
    f.write(tflite_model)

print(f"Model TensorFlow Lite został pomyślnie zapisany w pliku: {output_tflite_path}")

import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
import numpy as np

# Load the pre-trained MobileNetV2 model
model = MobileNetV2(weights='imagenet')

# Load and preprocess the image
img_path = 'image.jpeg'  # Replace this with the path to your .jpg image
try:
    img = image.load_img(img_path, target_size=(224, 224))  # MobileNetV2's input size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Predict the image class
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=3)[0]  # Get top 3 predictions
    print("Predictions:")
    for _, pred_class, pred_score in decoded_predictions:
        print(f"{pred_class}: {pred_score:.8f}")
except FileNotFoundError:
    print("Image file not found. Please provide the correct path.")
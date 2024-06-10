import tensorflow as tf
import cv2
import numpy as np

model = tf.keras.applications.MobileNetV2(weights="imagenet")

def recognize_target(image):
    processed_image = cv2.resize(image, (224, 224))
    processed_image = np.expand_dims(processed_image, axis=0)
    processed_image = tf.keras.applications.mobilenet_v2.preprocess_input(processed_image)
    
    predictions = model.predict(processed_image)
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)
    
    return decoded_predictions

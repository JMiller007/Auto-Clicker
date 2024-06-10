import cv2
import numpy as np

def process_image(image):
    image_np = np.array(image)
    gray_image = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
    return gray_image

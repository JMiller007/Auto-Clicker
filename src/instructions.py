import pytesseract
import cv2
import numpy as np

# Set the Tesseract executable path if it's not in your PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to extract text and their positions using Tesseract OCR
def extract_text_with_positions(image):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Use Tesseract to do OCR on the image
    data = pytesseract.image_to_data(gray_image, output_type=pytesseract.Output.DICT)
    
    # Extract the bounding boxes and text
    n_boxes = len(data['text'])
    boxes = []
    for i in range(n_boxes):
        if int(data['conf'][i]) > 60:  # Consider text with confidence > 60
            (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
            boxes.append((data['text'][i], x, y, w, h))
    
    # Print extracted text and their positions for debugging
    for i, (text, x, y, w, h) in enumerate(boxes):
        print(f"Detected text: '{text}' at position: ({x}, {y}, {w}, {h}) with confidence: {data['conf'][i]}")
    
    return boxes

# Function to find the phrase and get its position
def find_phrase_position(phrase, boxes):
    phrase = phrase.lower().strip().split()
    words_matched = 0
    start_position = None
    
    for i, (text, x, y, w, h) in enumerate(boxes):
        if phrase[words_matched] in text.lower():
            if words_matched == 0:
                start_position = (x + w // 2, y + h // 2)
            words_matched += 1
            if words_matched == len(phrase):
                return start_position
        else:
            words_matched = 0
            start_position = None
    
    return None, None

# Function to interpret the instruction and find the corresponding action
def interpret_instruction(instruction, image):
    boxes = extract_text_with_positions(image)
    actions = []
    instruction_parts = instruction.lower().split(" then ")
    
    for part in instruction_parts:
        if "double click on" in part:
            phrase = part.replace("double click on", "").strip()
            x, y = find_phrase_position(phrase, boxes)
            if x is not None and y is not None:
                actions.append(("double_click", x, y))
        elif "right click on" in part:
            phrase = part.replace("right click on", "").strip()
            x, y = find_phrase_position(phrase, boxes)
            if x is not None and y is not None:
                actions.append(("right_click", x, y))
        elif "click on" in part:
            phrase = part.replace("click on", "").strip()
            x, y = find_phrase_position(phrase, boxes)
            if x is not None and y is not None:
                actions.append(("click", x, y))
    
    return actions

# Example usage (for testing purposes)
if __name__ == "__main__":
    # Load a sample screen image
    screen_image = cv2.imread('screen_sample.png')

    # User instruction
    user_instruction = "click on Add Team workspace then click on Meaningful GitHub Projects"

    # Interpret the instruction
    actions = interpret_instruction(user_instruction, screen_image)

    for action in actions:
        print(f"Action: {action[0]}, Coordinates: ({action[1]}, {action[2]})")

# AI Auto Clicker

## Description

An AI-powered auto-clicker that interprets user instructions and performs actions on the screen based on text recognition.

## Features

- Capture the screen and analyze it for text positions.
- Interpret user instructions to click on specific text.
- Perform click, double-click, and right-click actions.
- User-friendly GUI for entering instructions.

## Requirements

- Python 3.6+
- OpenCV
- PyAutoGUI
- PyTesseract
- NumPy
- Tkinter

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/JMiller007/Auto-Clicker.git
   cd auto-clicker
   ```

2. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

3. Install Tesseract OCR. Instructions can be found [here](https://github.com/tesseract-ocr/tesseract).

## Usage

1. Run the `main.py` script:

   ```sh
   python src/main.py
   ```

2. Enter your instruction in the GUI window and click "Submit" to perform the action.

## Example Instructions

- `Click on New Chat`
- `Double click on Submit`
- `Right click on Options`

## File Structure

auto-clicker/
│
├── src/
│ ├── **init**.py
│ ├── main.py
│ ├── capture.py
│ ├── instructions.py
│ └── actions.py
│
├── requirements.txt
└── README.md

## Contributing

Contributions are welcome

## License

This project is licensed under the MIT License

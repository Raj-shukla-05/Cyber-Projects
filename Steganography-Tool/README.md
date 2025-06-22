# Steganography Tool for Image/File Hiding

## Introduction
A Python-based steganography tool that allows you to:
1. Hide secret text messages inside image files.
2. Extract hidden messages from stego-images.

## Features
- Encode text into image using Least Significant Bit (LSB) technique.
- Decode hidden messages from images.
- Command Line Interface (CLI) based.

## Tools & Technologies
- Python 3.x
- Libraries: `Pillow`, `argparse`

## How to Run
### 1. Install Dependencies
```bash
pip install pillow
```

### 2. Encode (Hide a Message)
```bash
python steganography_tool.py -e input_image.png output_image.png "SecretMessage"
```

### 3. Decode (Extract Message)
```bash
python steganography_tool.py -d output_image.png
```

## Example
```bash
python steganography_tool.py -e sample_image.png encoded_image.png "HiddenData123"
python steganography_tool.py -d encoded_image.png
```

## Project Structure
```
Steganography-Tool/
│
├── steganography_tool.py      # Main Python script
├── sample_image.png           # Sample image for testing
├── README.md                  # Project documentation
└── Steganography_Tool_Report.pdf  # Final report
```

## Note
This tool is intended for **educational and ethical purposes only**.

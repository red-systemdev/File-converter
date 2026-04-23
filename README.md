# Image to PDF Converter

A simple Python script that converts one or multiple images into a single PDF file using the Pillow library.

## Features
- Convert multiple images into one PDF
- Supports JPG, JPEG, PNG
- Maintains image order
- Lightweight and easy to use

## Requirements
- Python 3.x
- Pillow

Install Pillow:
pip install pillow

## Usage
1. Add your image paths in the script:
image_files = [
    "image1.jpg",
    "image2.png",
    "image3.jpeg"
]

2. Run the script:
python script.py

3. Output:
output.pdf will be created in the same folder

## Script
from PIL import Image

def images_to_pdf(image_paths, output_pdf):
    images = []

    for img_path in image_paths:
        img = Image.open(img_path)

        if img.mode != 'RGB':
            img = img.convert('RGB')

        images.append(img)

    if not images:
        print("No valid images found.")
        return

    images[0].save(
        output_pdf,
        save_all=True,
        append_images=images[1:]
    )

    print(f"PDF saved as: {output_pdf}")

if __name__ == "__main__":
    image_files = [
        "image1.jpg",
        "image2.png",
        "image3.jpeg"
    ]

    output_file = "output.pdf"

    images_to_pdf(image_files, output_file)

## Notes
- Ensure file paths are correct
- Images are converted to RGB to prevent errors
- Order of images determines PDF order

## License
Free to use

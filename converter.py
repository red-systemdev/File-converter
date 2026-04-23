from PIL import Image
import os

def images_to_pdf(image_paths, output_pdf):
    images = []

    for path in image_paths:
        if not os.path.exists(path):
            print(f"File not found: {path}")
            continue

        img = Image.open(path)

        # Convert all images to RGB (required for PDF)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        images.append(img)

    if not images:
        print("No valid images to convert.")
        return

    # Save first image and append the rest
    first_image = images[0]
    rest_images = images[1:]

    first_image.save(
        output_pdf,
        save_all=True,
        append_images=rest_images
    )

    print(f"PDF created successfully: {output_pdf}")


# Example usage
if __name__ == "__main__":
    image_files = [
        "image1.jpg",
        "image2.png",
        "image3.jpeg"
    ]

    output_file = "output.pdf"
    images_to_pdf(image_files, output_file)

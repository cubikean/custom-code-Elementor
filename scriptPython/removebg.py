import os
import sys
from rembg import remove
from PIL import Image

def remove_background(image_path):
    try:
        print(f"Processing image: {image_path}")
        input_image = Image.open(image_path)
        output_image = remove(input_image)
        output_path = os.path.splitext(image_path)[0] + "_no_bg.png"
        output_image.save(output_path)
        print(f"Saved without background: {output_path}")
    except Exception as e:
        print(f"Error processing {image_path}: {e}", file=sys.stderr)

def process_images(image_paths):
    for image_path in image_paths:
        remove_background(image_path)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image_paths = sys.argv[1:]
        process_images(image_paths)
    else:
        print("No images provided.", file=sys.stderr)

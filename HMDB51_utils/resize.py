#!/usr/bin/env python3
"""
Script to resize example frames of all videos.
"""
import os
import sys
from PIL import Image

def resize(image_path: str, size: tuple[int] = (320,320)) -> None:
    """Resize the image to the given size and save it."""
    try:
        with Image.open(image_path) as img:
            img = img.resize(size)
            img.save(image_path)
            print(f"Resized and saved image: {image_path}")
    except Exception as e:
        print(f"Error resizing image {image_path}: {e}")

def main(input_dir: str):
    if not os.path.isdir(input_dir):
        raise ValueError(f"{input_dir} is not a directory.")
    for root, dirs, files in os.walk(input_dir):
        for f in files:
            if f.endswith('.jpg'):
                image_path = os.path.join(root, f)
                resize(image_path)

if __name__ == '__main__':
    main(sys.argv[1])
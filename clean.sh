#!/bin/bash

# Directory to search for images
IMAGE_DIR="/workspace"

# Find all image files (adjust the pattern to include the image types you have)
find "$IMAGE_DIR" -type f \( -iname \*.jpg -o -iname \*.png -o -iname \*.gif \) | while read -r file; do
  # Get the dimensions of the image
  dimensions=$(identify -format "%wx%h" "$file")
  # Check if dimensions are not 320x240
  if [ "$dimensions" != "320x240" ]; then
    # Delete the file
    rm "$file"
    echo "Deleted $file with dimensions $dimensions"
  fi
done
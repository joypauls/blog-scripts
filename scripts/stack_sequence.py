import os
import argparse
import cv2
from typing import List
import numpy as np

SEQUENCE_PATH = "./data/low_light_sequence_20231227/processed/iso1600"
OUTPUT_PATH = "./data/low_light_sequence_20231227/processed/iso1600/stack"

STACK_SEQUENCE = [2, 4, 8, 16, 32, 64]


def stack_images(images: List[np.ndarray]) -> np.ndarray:
    stack = np.stack(images)
    return np.mean(stack, axis=0)


def main():
    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_PATH, exist_ok=True)

    print("reading")
    images = []
    # Iterate over all files in the input directory
    for filename in os.listdir(SEQUENCE_PATH):
        if filename.endswith(".png"):
            # Read the image
            image_path = os.path.join(SEQUENCE_PATH, filename)
            image = cv2.imread(image_path)
            images.append(image)

    print("stacking")
    for i in STACK_SEQUENCE:
        stacked_image = stack_images(images[0:i])
        output_path = os.path.join(OUTPUT_PATH, f"mean_image_{i}_frames.png")
        cv2.imwrite(output_path, stacked_image)


if __name__ == "__main__":
    main()

import os
import argparse
import cv2

RAW_PATH = "./data/low_light_sequence_20231227/raw/iso6400"
PROCESSED_PATH = "./data/low_light_sequence_20231227/processed/iso6400"


def process_directory(x: int, y: int, width: int, height: int):
    # Create output directory if it doesn't exist
    os.makedirs(PROCESSED_PATH, exist_ok=True)

    # Iterate over all files in the input directory
    for filename in os.listdir(RAW_PATH):
        if filename.endswith(".png"):
            # Read the image
            image_path = os.path.join(RAW_PATH, filename)
            image = cv2.imread(image_path)

            # Crop the image
            cropped_image = image[y : y + height, x : x + width]

            # Save the cropped image
            output_path = os.path.join(PROCESSED_PATH, filename)
            cv2.imwrite(output_path, cropped_image)

            print(f"Cropped {filename} and saved to {output_path}")


if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=int)
    parser.add_argument("y", type=int)
    parser.add_argument("width", type=int)
    parser.add_argument("height", type=int)
    args = parser.parse_args()

    # Call the crop_images function with the provided arguments
    process_directory(args.x, args.y, args.width, args.height)

from PIL import Image
import os

def split_image(input_image_path, output_folder, start_counter):
    image = Image.open(input_image_path)
    width, height = image.size
    base_filename = os.path.splitext(os.path.basename(input_image_path))[0]
    
    # Set the square size to 101x101
    square_size = 101
    
    counter = start_counter  # Start the counter from 1500

    for i in range(0, width, square_size):
        for j in range(0, height, square_size):
            left = i
            upper = j
            right = min(i + square_size, width)
            lower = min(j + square_size, height)
            cropped_image = image.crop((left, upper, right, lower))
            output_image_path = os.path.join(output_folder, f"{counter}.jpg")  # Save as JPEG
            cropped_image.save(output_image_path, "JPEG")  # Use "JPEG" format
            counter += 1

if __name__ == "__main__":
    input_image_path = r"C:\Users\jmedh\Downloads\12.jpg"  # Provide the path to your large JPEG image
    output_folder = "output_folder11"  # Provide the path to the folder where you want to save the smaller squares
    start_counter = 1500  # Start the counter from 1500

    os.makedirs(output_folder, exist_ok=True)
    split_image(input_image_path, output_folder, start_counter)

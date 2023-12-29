from PIL import Image
import os


def resize_and_crop(img, target_size):
    """Resize and crop an image to fit the target size."""
    # Calculate the target aspect ratio and the image aspect ratio
    target_ratio = target_size[0] / target_size[1]
    img_ratio = img.size[0] / img.size[1]

    # Resize and then crop the image to fit the target size
    if target_ratio > img_ratio:  # Image is too tall
        resized_img = img.resize((target_size[0], int(target_size[0] / img_ratio)), Image.Resampling.LANCZOS)
        top = int((resized_img.size[1] - target_size[1]) / 2)
        cropped_img = resized_img.crop((0, top, target_size[0], top + target_size[1]))
    else:  # Image is too wide
        resized_img = img.resize((int(target_size[1] * img_ratio), target_size[1]), Image.Resampling.LANCZOS)
        left = int((resized_img.size[0] - target_size[0]) / 2)
        cropped_img = resized_img.crop((left, 0, left + target_size[0], target_size[1]))

    return cropped_img


def load_images_from_folder(folder):
    """Load all images from a folder."""
    images = []
    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename)
        try:
            with Image.open(img_path) as img:
                images.append(img.copy())
        except:
            print(f"Failed to load image: {img_path}")
    return images


def create_grid_mosaic(images, grid_size, tile_size):
    """Create a grid mosaic from the list of images."""
    mosaic_image = Image.new('RGB', (grid_size[0] * tile_size[0], grid_size[1] * tile_size[1]))

    for i, img in enumerate(images):
        if i >= grid_size[0] * grid_size[1]:
            break
        x = (i % grid_size[0]) * tile_size[0]
        y = (i // grid_size[0]) * tile_size[1]
        resized_img = resize_and_crop(img, tile_size)
        mosaic_image.paste(resized_img, (x, y))

    return mosaic_image


# # Main program
# folder = '/Users/vincenzotranquillo/Desktop/Wedding Album/City Portraits'  # Replace with your images folder path
# images = load_images_from_folder(folder)
#
# grid_size = (10, 10)  # Define your grid size (columns, rows)
# tile_size = (100, 100)  # Define the size for each tile (width, height)
# final_mosaic = create_grid_mosaic(images, grid_size, tile_size)
#
# output_file = 'grid_mosaic.jpg'
# final_mosaic.save(output_file)
# print("Grid mosaic created and saved as", output_file)

from PIL import Image
import os

# ... [Other functions like resize_and_crop, create_grid_mosaic remain the same]

def main():
    # Ask the user for the path to the images
    folder = input("Please enter the path to your images: ")

    # Check if the provided path is valid
    if not os.path.exists(folder):
        print("The provided path does not exist. Please check and try again.")
        return

    # Load and process the images
    images = load_images_from_folder(folder)
    if not images:
        print("No images found in the specified folder.")
        return

    # Define grid size and tile size
    grid_size = (18, 12)  # You can also ask the user for these values
    tile_size = (100, 100)  # Same as above

    # Create and save the mosaic
    final_mosaic = create_grid_mosaic(images, grid_size, tile_size)
    output_file = 'grid_mosaic.jpg'
    final_mosaic.save(output_file)
    print("Grid mosaic created and saved as", output_file)

# Run the main function
if __name__ == "__main__":
    main()


# /Users/vincenzotranquillo/Desktop/Wedding Album/City Portraits

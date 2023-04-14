from PIL import Image, ImageEnhance, ImageFilter
import os


class Editor:
    def __init__(self):
        self.path = "./imgs"
        self.pathOut = "/editedImgs"
        """Paths for img editor and path to folder for output imgs after edit"""

    def file_handle(self):
        """For loop for editting each img and putting it to output folder"""
        for filename in os.listdir(self.path):
            img = Image.open(f"{self.path}/{filename}")
            edit = img.filter(ImageFilter.SHARPEN).convert(
                "L")  # Apply filter SHARPEN, convert for color mode-L for b&w
            factor = 1.5  # Intensity of enhance
            enhancer = ImageEnhance.Contrast(edit)  # Define Contrast in file from variable edit
            edit = enhancer.enhance(factor)  # Apply Contrast in file from variable edit
            clean_name = os.path.splitext(filename)[0]  # Cleaning name of the file to match starting name
            edit.save(f".{self.pathOut}/{clean_name}_edited.jpg")  # Saving the img to the defined folder
            return "Done"

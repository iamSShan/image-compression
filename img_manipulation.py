import os
import tinify
from PIL import Image


tinify.key = ""  # Refer to this page to create --> https://tinypng.com/developers

def start_optimization(input_file):
    """
	https://tinypng.com/developers
	Presently limit for compressing images per month is 500(Dated: 29-06-2018). It may change afterwards.
	"""

    src = tinify.from_file(input_file)
    src.to_file("output/optimized.jpg")
    # src= tinify.from_url("enter image url here")

def handle_decrement(location):
	w = int(input("Please enter width\n"))
	h = int(input("Please enter height\n"))
	image = Image.open(location)

	new_img = image.resize((w, h))
	new_img.save('output/out_'+os.path.basename(location), optimize=True, quality=85)
	print("DONE!!")


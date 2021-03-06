import sys
import os
from PIL import Image, ImageFilter
# from PIL ImageFilter

image_folder = sys.argv[1]
output_images = sys.argv[2]

# print(image_folder, output_images)
# Should print images/ new/
# images/ sys.argv[1]
# new/ sys.argv[2]

# python is sys.argv[0], which is never expressed since,
# it is used as the initial argument in python. It would be as if, 
# sys,argv[0] is redundant, and that the computer knows it's python.

def make_dir(output_images):
    if not os.path.exists(output_images):
        os.makedirs(output_images)
# the output_images would be considered the sys.argv[3], without being
# explicit about the statement, as os is doing the work to produce that folder.
# The folder produced would be a folder that can be named anything,
# such as png_images.

def main(args):
    make_dir(output_images)
    for filename in os.listdir(image_folder):
        img = Image.open(f'./{image_folder}{filename}')
        reduced_name = os.path.splitext(filename)[0]
        img.save(f'{output_images}{reduced_name}.png', 'png')
        img.thumbnail((150,150))
        print(img.size, "success")
        # print('success!!!')
        img.show()


if __name__ == '__main__':
    main(sys.argv[1:])
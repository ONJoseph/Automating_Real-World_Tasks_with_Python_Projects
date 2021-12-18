"""
How to Use PIL for Working With Images:
For example, if we wanted to resize an image and save the new image with a new name, we could do it with:
from PIL import Image
im = Image("example.jpg")
new_im = im.resize((640,480))
new_im.save("example_resized.jpg")
In this case, we're using the resize method that returns a new image with the new size, and then we save it into a different file. Or, if we want to rotate an image, we can use code like this:
from PIL import Image
im = Image("example.jpg")
new_im = im.rotate(90)
new_im.save("example_rotated.jpg")
This method also returns a new image that we can then use to create the new rotated file. Because the methods return a new object, we can even combine these operations into just one line that rotates, resizes, and saves:
from PIL import Image
im = Image("example.jpg")
im.rotate(180).resize((640,480)).save("flipped_and_resized.jpg")
"""

"""
~Commands:
Download the file:
~curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=$11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" > /dev/null | curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" -o images.zip && sudo rm -rf cookie
List files using the command:
~ls
Unzip the file using the following command:
~unzip images.zip
To list images from the images folder use the following command:
~ls ~/images
Install Pillow
We should change the format and size of these pictures, and rotate them by 90° clockwise. To do this, we'll use Python Imaging Library (PIL). Install pillow library using the following command:
~pip3 install pillow
Write a Python script:
~nano fix_python.py
~chmod +x fix_image.py
~./fix_image.py
~ls /opt/icons
~python3
~from PIL import Image
~img = Image.open("/opt/icons/ic_edit_location_black_48dp")
~img.format, img.size
~exit()
"""
#script Below

#!/usr/bin/env python3
import os
from PIL import Image
old_path = os.path.expanduser('~') + '/images/'
new_path = '/opt/icons/'
for image in os.listdir(old_path):
        if '.' not in image[0]:
                img = Image.open(old_path + image)
                img.rotate(-90).resize((128,
128)).convert("RGB").save(new_path + image.split('.')[0], 'jpeg')
                img.close()

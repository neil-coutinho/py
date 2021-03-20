#!/usr/bin/env python3
from PIL import Image
import os

dir = os.listdir("images")
#print(dir)
for img in dir:
        img_path = os.path.join("images", img)
        img_item = Image.open(img_path)
        if img_item.format == "TIFF":
                print(img_item.format)
                #print("{} - {}".format(img, item))
                transformed_img = img_item.rotate(90).resize((128,128))
                #print(transformed_img.size)
                transformed_img.convert("RGB").save("/opt/icons/"+img+".jpeg")
#print("Hello World")
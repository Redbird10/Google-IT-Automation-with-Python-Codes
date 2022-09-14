#!/usr/bin/env python3
from PIL import Image
import os
pic_list = os.listdir("./supplier-data/images")
for every_image in pic_list:
  if every_image.endswith("tiff"):
    with Image.open("./supplier-data/images/"+str(every_image)) as im:
      im.convert("RGB").resize((600,400)).save("./supplier-data/images/"+str(every_image)[:-5]+".jpeg")

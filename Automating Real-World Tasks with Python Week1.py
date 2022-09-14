#!/usr/bin/env python3
from PIL import Image
import os
pic_list = os.listdir("./images")
try:
  os.mkdir("/opt/icons/")
except:
  pass
for every_image in pic_list:
  with Image.open("./images/"+str(every_image)) as im:
    im.rotate(90).resize((128,128)).convert("RGB").save("/opt/icons/"+str(every_image)+".jpeg")

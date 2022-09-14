#!/usr/bin/env python3
import os
import requests
#Using Requests module to upload file
pic_list = os.listdir("./supplier-data/images")
url = "http://localhost/upload/"
for every_image in pic_list:
  if every_image.endswith("jpeg"):
    with open('./supplier-data/images/'+every_image, 'rb') as opened:
      r = requests.post(url, files={'file': opened})

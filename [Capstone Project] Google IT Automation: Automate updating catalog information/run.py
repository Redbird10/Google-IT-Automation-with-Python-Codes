#! /usr/bin/env python3
import os
import requests
path = "./supplier-data/descriptions/"
ip_address="35.224.16.161"
files = os.listdir(path)
upload_list=[]
for file in files:
  with open(path+str(file)) as f:
    content=f.read().splitlines()
    dict0={}
    dict0["name"]=content[0]
    dict0["weight"]=int(content[1].split()[0])
    dict0["description"]=content[2]
    dict0["image_name"]=file[:-4]+".jpeg"
    upload_list.append(dict0)
for fruit in upload_list:
  response = requests.post("http://35.224.16.161/fruits/", json=fruit)
  response.raise_for_status()

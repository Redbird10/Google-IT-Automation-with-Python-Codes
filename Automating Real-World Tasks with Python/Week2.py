#! /usr/bin/env python3
import os
import requests
path = "/data/feedback/"
ip_address="34.132.119.183"
files = os.listdir(path)
review_list=[]
for file in files:
  with open(path+str(file)) as f:
    content=f.read().splitlines()
    dict0={}
    dict0["title"]=content[0]
    dict0["name"]=content[1]
    dict0["date"]=content[2]
    dict0["feedback"]=content[3]
    review_list.append(dict0)
for p in review_list:
  response = requests.post("http://34.132.119.183/feedback/", json=p)
  response.raise_for_status()

#!/usr/bin/env python3

import os
import requests
data = {}
files = os.listdir("/data/feedback/")
#print(files)
for file in files:
        #print(file)
        
        with open(os.path.join("/data/feedback",file), "r") as f:
                #print(f.readlines())
                line = f.readlines()
                #print(line)
                data["title"] = line[0]
                data["name"] = line[1]
                data["date"] = line[2]
                data["feedback"] = line[3]
                print(data)
        f.close()
        res = requests.post("http://35.192.53.88/feedback/", data=data)
        print(res)
        print(res.status_code)
        print(res.ok)

        if(res.ok):
                print("Status: {}. Feedback uploaded".format(res.status_code))
        else:
                print("Something went wrong")

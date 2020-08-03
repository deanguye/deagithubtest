# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 18:27:59 2020

@author: dnguy
"""
import requests
apirequest=requests.get("https://api.github.com")
x=apirequest.status_code
if x == 200:
    print("success")
else:
    print("issue detected")    


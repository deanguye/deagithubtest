# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 16:48:00 2020

@author: dnguy
"""

##This is a code I practiced from w2schools.com##
import requests
requestapi=requests.get("https://api.github.com")
print("API request response: ",requestapi)
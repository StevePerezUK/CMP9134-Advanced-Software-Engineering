#!/usr/bin/env python3

import re

def get_input():
    instring= input("Please enter a string with - \"not bad\" in it ")
    newstring = instring.replace("not bad", "good")
    print("{}".format(newstring))

get_input()
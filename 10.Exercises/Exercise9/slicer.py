#!/usr/bin/env python3

def get_input():
    in_string= input("Please enter a string: ")
    first_three = in_string[:3]
    last_three = in_string[len(in_string)-3:]
    print("First three characters = {}".format(first_three))
    print("Last three characters = {}".format(last_three))

get_input()
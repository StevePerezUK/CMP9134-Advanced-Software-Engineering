#!/usr/bin/env python3

# def get_input():
#     in_string= input("Please enter a string: ")
#     first_three = in_string[:3]
#     last_three = in_string[len(in_string)-3:]
#     print("First three characters = {}".format(first_three))
#     print("Last three characters = {}".format(last_three))

# get_input()

class GetInput(object):

    def __init__(self):
        self._instring = ""
        
    def get_input(self):
        self._instring = input("Please enter a string: ")
        
class GetSlices(GetInput):

    def __init__(self):
        super().__init__()
        self.get_input()
        self._first_three = ""
        self._last_three = ""

    def slice_string(self):
        self._first_three = self._instring[:3]
        self._last_three = self._instring[len(self._instring)-3:]
        
class SliceString(GetSlices):

    def __init__(self):
        super().__init__()
        self.slice_string()

    def print_slices(self):
        print("First three characters = {}".format(self._first_three))
        print("Last three characters = {}".format(self._last_three))        

string_slice = SliceString()
string_slice.print_slices()



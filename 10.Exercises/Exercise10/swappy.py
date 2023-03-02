#!/usr/bin/env python3


# def get_input():
#     string1 = input("Please enter a string: ")
#     string2 = input("Please enter another string: ")
#     # Sample String : 'abc', 'xyz' 
#     # Expected Result : 'xyc abz'

#     print("{0}{1} {2}{3}".format(string2[:2],string1[2:],string1[:2],string2[2:]))

# if __name__ == "__main__":
#     get_input()


class GetInput(object):

    def __init__(self):
        self._s1 = ""
        self._s2 = ""

    def get_input(self):
        self._s1 = input("Please enter a string: ")
        self._s2 = input("Please enter another string: ")
   
class CalcStrings(GetInput):

    def __init__(self):
        super().__init__()
        self.get_input()
        self._outstring = ""
        self._outstring1 = ""
        self._outstring2 = ""


    def swap_strings(self):
        self._outstring = "{0}{1} {2}{3}".format(self._s2[:2],self._s1[2:],self._s1[:2],self._s2[2:])


class SwapStrings(CalcStrings):

    def __init__(self):
        super().__init__()
        self.swap_strings()
        

    def print(self):
        print("{0}".format(self._outstring))            

swap_strings = SwapStrings()
swap_strings.print()


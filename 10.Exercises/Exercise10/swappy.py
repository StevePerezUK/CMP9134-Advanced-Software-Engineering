#!/usr/bin/env python3


def get_input():
    string1 = input("Please enter a string: ")
    string2 = input("Please enter another string: ")
    # Sample String : 'abc', 'xyz' 
    # Expected Result : 'xyc abz'

    print("{0}{1} {2}{3}".format(string2[:2],string1[2:],string1[:2],string2[2:]))

if __name__ == "__main__":
    get_input()
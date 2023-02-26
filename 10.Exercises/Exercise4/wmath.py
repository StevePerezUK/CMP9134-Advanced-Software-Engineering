#!/usr/bin/env python3

# function version

# a = 1.14
# b = a + 2
# a = b*4
# b = a/3.14
# c = b-8

# print("a = {0}, b = {1} c = {2}".format(a,b,c))

# OOP version

class WMaths(object):

    def __init__(self):
        self.a = 1.14
        self.b = 0
        self.c = 0

    def first_pass(self):
        self.b = self.a + 2
        self.a = self.b * 4

    def second_pass(self):
        self.b = self.a / 3.14
        self.c = self.b - 8

class PrintMaths(WMaths):

    def print(self):
        self.first_pass()
        self.second_pass()
        print("a = {0}, b = {1} c = {2}".format(self.a,self.b,self.c))                 


wmath= PrintMaths()
wmath.print()

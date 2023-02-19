#!/usr/bin/env python3

import math as m

def get_dimensions():
    radius= input("Please enter the radius of the circle: ")
    radius = float(radius)

    circum= m.pi * square(radius)
    area = 2 * m.pi * radius

    print("Area = %s" %(area))
    print("Circumference = %s" %(circum))


def square(num):
    return num ** 2

get_dimensions()



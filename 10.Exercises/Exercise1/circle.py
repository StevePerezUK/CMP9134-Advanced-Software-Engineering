#!/usr/bin/env python3



class Circle(object):

    def __init__(self):
        self.area= float(0)
        self.radius= int(0)
        self.circumference= float(0)

    def set_radius(self,radius):
        import math as m
        
        self.radius = float(radius)
        self.circumference = m.pi * self.square(self.radius)
        self.area = 2 * m.pi * self.radius

    def square(self,number):
        return number ** 2


class PrintCircle(Circle):

    def show(self):
        print("Circle Dimensions for a radius of %s" %(self.radius))
        print("Area = {}".format(self.area))
        print("Circumference = {}".format(self.circumference))

class RCircle(PrintCircle):

    def get_radius(self):
        try: 
            self.radius = input("Please enter the radius of the Circle: ")
        except ValueError:
            print("ERROR: Number was invalid")
            return 1
        self.set_radius(self.radius)
        self.show()

show_circle = RCircle()
show_circle.get_radius()






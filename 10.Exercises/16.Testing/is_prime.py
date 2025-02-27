#!/usr/bin/env python3

import math

def is_prime(num):
    
    '''Check if num is prime or not.'''
    if type(num) != int:
        raise TypeError('num is of invalid type')
    if num < 0:
        raise ValueError('Check the value of num; is num a non-negative?')
    
    '''Check if num is prime or not.'''
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True
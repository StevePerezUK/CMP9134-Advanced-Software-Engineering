#!/usr/bin/env python3

def get_input():
    c_prompt= "Please enter an integer for {}: " 
    rtn={}
    rtn['x'] = int(input(c_prompt.format("x")))
    rtn['y'] = int(input(c_prompt.format("y")))
    rtn['z'] = int(input(c_prompt.format("z")))

    return rtn

def truth_decode(inputs):
    statement1 = False
    statement2 = False
    statement3 = False
    if (inputs['x'] < inputs['y']) or (inputs['y'] > inputs['z']):
        statement1 = True    
    print("\tx < y or y > z is \t\t{}".format(statement1))
    
    if inputs['y'] != inputs['z']:
        statement2 = True
    print("\ty != z is \t\t\t{}".format(statement2))

    if (inputs['x'] >= inputs['z']) or (inputs['y'] > inputs['z']) and (inputs['x'] != inputs['y']):
        statement3 = True
    print("\tx >= z or y > z and x != y is \t{}".format(statement3))


if __name__ == "__main__":
    truth_decode(get_input())

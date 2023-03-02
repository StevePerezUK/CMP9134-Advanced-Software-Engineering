#!/usr/bin/env python3

# def get_input():
#     c_prompt= "Please enter an integer for {}: " 
#     rtn={}
#     rtn['x'] = int(input(c_prompt.format("x")))
#     rtn['y'] = int(input(c_prompt.format("y")))
#     rtn['z'] = int(input(c_prompt.format("z")))

#     return rtn

# def truth_decode(inputs):
#     statement1 = False
#     statement2 = False
#     statement3 = False
#     if (inputs['x'] < inputs['y']) or (inputs['y'] > inputs['z']):
#         statement1 = True    
#     print("\tx < y or y > z is \t\t{}".format(statement1))
    
#     if inputs['y'] != inputs['z']:
#         statement2 = True
#     print("\ty != z is \t\t\t{}".format(statement2))

#     if (inputs['x'] >= inputs['z']) or (inputs['y'] > inputs['z']) and (inputs['x'] != inputs['y']):
#         statement3 = True
#     print("\tx >= z or y > z and x != y is \t{}".format(statement3))


# if __name__ == "__main__":
#     truth_decode(get_input())


class GetInput(object):

    def __init__(self):
        self._numbers = {}

    def get_input(self):
        c_prompt= "Please enter an integer for {}: " 
        self._numbers['x'] = int(input(c_prompt.format("x")))
        self._numbers['y'] = int(input(c_prompt.format("y")))
        self._numbers['z'] = int(input(c_prompt.format("z")))


class CalculateLogic(GetInput):

    def __init__(self):
        super().__init__()
        self.get_input()
        self._statements = {
            '1' : False,
            '2' : False,
            '3' : False
        }        
        
    def truth_decode(self):
        inp= self._numbers
        if (inp['x'] < inp['y']) or (inp['y'] > inp['z']):
            self._statements['1'] = True 
        if inp['y'] != inp['z']:
            self._statements['2'] = True
        if (inp['x'] >= inp['z']) \
            or  (inp['y'] >  inp['z']) \
            and (inp['x'] != inp['y']):
            self._statements['3'] = True
    
class ValidateStatements(CalculateLogic):

    def __init__(self):
        super().__init__()
        self.truth_decode()

    def print(self):
        print("\tx < y or y > z is \t\t{}".format(self._statements['1']))    
        print("\ty != z is \t\t\t{}".format(self._statements['2']))
        print("\tx >= z or y > z and x != y is \t{}".format(self._statements['3']))

validate_statements = ValidateStatements()
validate_statements.print()



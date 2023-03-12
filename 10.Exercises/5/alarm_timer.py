#!/usr/bin/env python3

# def get_input():
#     print("This program will give you the hour your alarm will go off\n")
#     hours = {
#         'start_hour': 0, 
#         'future_hours': 0
#     } 
#     while True:
#         try:
#             hour= input("Please enter the current hour in two digits: ")
#             if int(hour) > 24 or int(hour) < 0:
#                 raise Exception 
#         except:
#             print("Please enter a number between 0 and 24")
#             continue
#         break
#     hours['start_hour'] = hour
#     while True:
#         try:
#             add_hours = input("Please enter the number of hours till the alarm will activate: ")
#             if int(add_hours) < 0:
#                 raise Exception
#         except:
#             print("Enter an integer for number of hours")
#             continue
#         break
#     hours['future_hours']= add_hours
    
#     return hours

# def calculate_hour(hours_dict):
#     alarm_hour = (int(hours_dict['start_hour']) + int(hours_dict['future_hours'])) % 24
#     print("Your alarm will sound at {:02}:00".format(alarm_hour))

# if __name__ == "__main__":
#     calculate_hour(get_input())


class GetInput(object):
    
    def __init__(self):
        self.start_hours = 0
        self.future_hours = 0
        self.current_hour = 0

    def get_inputs(self):
        while True:
            try:
                self.current_hour= input("Please enter the current hour in two digits: ")
                if int(self.current_hour) > 24 or int(self.current_hour) < 0:
                    raise Exception
                if not len(self.current_hour) == 2:
                    raise Exception 
            except:
                print("Please enter a number between 00 and 24")
                continue
            break
        while True:
            try:
                self.future_hours = input("Please enter the number of hours till the alarm will activate: ")
                if int(self.future_hours) < 0:
                    raise Exception
            except:
                print("Please enter an integer for number of hours")
                continue
            break

class CalculateHours(GetInput):

    def __init__(self):
        super().__init__()
        self.get_inputs()
        self.alarm_hour = 0
    
    def calculate_hours(self):
        self.alarm_hour = (int(self.current_hour) + int(self.future_hours)) % 24
    
class GiveAnswer(CalculateHours):
    
    def __init__(self):
        super().__init__()
        self.calculate_hours()

    def print_answer(self):
        print("Your alarm will sound at {:02}:00".format(self.alarm_hour))


sleep_timer = GiveAnswer()
sleep_timer.print_answer()



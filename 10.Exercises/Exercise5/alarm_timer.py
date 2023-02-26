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
    pass

class CalculateHours(GetInput):
    pass

class GiveAnswer(CalculateHours):
    pass
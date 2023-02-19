#!/usr/bin/env python3

import sys

c_weekdays = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

def get_input():
    print("Welcome to the holiday day checker\n")
    print("This will calculate the day of the week your will return from holiday")
    print("Sunday = 0 and Saturday = 6\n")
    holidays ={}
    while True:
        try:
            departure_day = int(input("Please enter your departure day of the week (0-6): "))
            if departure_day < 0 or departure_day > 6:
                print("Please enter an integer from 0 to 6 \n")
                continue
        except:
             print("Please enter an integer from 0 to 6 \n")
             continue
        break
    holidays['departure_day'] = departure_day
    while True:
        try:
            holiday_days = int(input("Please enter the number of days you will be away: "))
            if holiday_days <= 0:
                print("Please enter a postive integer")
                continue
        except:
            print("Please enter a positive integer")
            continue
        break
    holidays['days_away'] = holiday_days
    return holidays

def calculate_days(days):
    return_day = (days['departure_day'] + days['days_away']) % 7
    departure_weekday= c_weekdays[int(days['departure_day'])]
    return_weekday= c_weekdays[int(return_day)]
    print("\n\nYou are leaving for holiday on a {0} and returning on a {1}\n\n".format(departure_weekday,return_weekday))
    
if __name__ == "__main__":
    calculate_days(get_input())




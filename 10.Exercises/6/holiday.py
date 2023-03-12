#!/usr/bin/env python3

# Function version
# c_weekdays = [
#     "Sunday",
#     "Monday",
#     "Tuesday",
#     "Wednesday",
#     "Thursday",
#     "Friday",
#     "Saturday"
# ]

# def get_input():
#     print("Welcome to the holiday day checker\n")
#     print("This will calculate the day of the week your will return from holiday")
#     print("Sunday = 0 and Saturday = 6\n")
#     holidays ={}
#     while True:
#         try:
#             departure_day = int(input("Please enter your departure day of the week (0-6): "))
#             if departure_day < 0 or departure_day > 6:
#                 print("Please enter an integer from 0 to 6 \n")
#                 continue
#         except:
#              print("Please enter an integer from 0 to 6 \n")
#              continue
#         break
#     holidays['departure_day'] = departure_day
#     while True:
#         try:
#             holiday_days = int(input("Please enter the number of days you will be away: "))
#             if holiday_days <= 0:
#                 print("Please enter a postive integer")
#                 continue
#         except:
#             print("Please enter a positive integer")
#             continue
#         break
#     holidays['days_away'] = holiday_days
#     return holidays

# def calculate_days(days):
#     return_day = (days['departure_day'] + days['days_away']) % 7
#     departure_weekday= c_weekdays[int(days['departure_day'])]
#     return_weekday= c_weekdays[int(return_day)]
#     print("\n\nYou are leaving for holiday on a {0} and returning on a {1}\n\n".format(departure_weekday,return_weekday))
    
# if __name__ == "__main__":
#     calculate_days(get_input())


# OOP version

class GetInput(object):
    
    def __init__(self):
        self.departure_day = 0
        self.holiday_days = 0

    def get_inputs(self):
        print("Welcome to the holiday day checker\n")
        print("This will calculate the day of the week your will return from holiday")
        print("Sunday = 0 and Saturday = 6\n")
        while True:
            try:
                self.departure_day = int(input("Please enter your departure day of the week (0-6): "))
                if self.departure_day < 0 or self.departure_day > 6:
                    raise Exception
            except Exception:
                print("Please enter an integer from 0 to 6 \n")
                continue
            break

        while True:
            try:
                self.holiday_days = int(input("Please enter the number of days you will be away: "))
                if self.holiday_days <= 0:
                    raise Exception
            except Exception:
                print("Please enter a positive integer")
                continue
            break
    
class CalculateDays(GetInput):

    def __init__(self):
        super().__init__()
        self.get_inputs()
        self.return_day = 0
        self.departure_weekday = ""
        self.return_weekday = ""

    def calculate_days(self):
        self.return_day = (self.departure_day + self.holiday_days) % 7
        self.departure_weekday= self.get_weekday(self.departure_day) 
        self.return_weekday= self.get_weekday(self.return_day)
    
    def get_weekday(self,day):
        week_days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        if day > 6 or day < 0:
            print("Invalid day, must be between 0 and 6")
            return False
        return week_days[day]
        

class PrintWeekdays(CalculateDays):

    def __init__(self):
        super().__init__()
        self.calculate_days()

    def print_days(self):
        print("\n\nYou are leaving for holiday on a {0} and returning on a {1}\n\n".format(self.departure_weekday,self.return_weekday))
            

        
days = PrintWeekdays()
days.print_days()




#!/usr/bin/env python3

# import sys

# def get_months():

#     start_months = [
#         'January', 
#         'March', 
#         'May',
#         'September', 
#         'December',
#     ]
#     remove_list = [
#      'May',
#      'September',
#      'October'   
#     ]

#     input_month = ""

#     while True:
#         print("Current list of months")
#         print("{}".format(start_months))
#         input_month= input("Enter month: ")
#         if not valid_month(input_month,start_months):
#             print("{0} is not a valid month name - try again".format(input_month))
#             continue
#         x = start_months.append(input_month)
#         if len(start_months) == 12:
#             print("Current list of months")
#             print("{}".format(start_months))
#             break
#         else: 
#             print("Current month list is {} months".format(len(start_months)))
#             continue
    
#     for el in remove_list:
#         print("Removing {} from the month list".format(el))
#         start_months.remove(el)
    
#     print("Final list of months = {}".format(start_months))

# def valid_month(chk_month,input_list):
#     c_all_months = [
#         'January',
#         'February', 
#         'March', 
#         'April',
#         'May',
#         'June',
#         'July',
#         'August',
#         'September',
#         'October',
#         'November', 
#         'December'
#     ]

#     valid_month= False
#     for month in input_list:
#         if month == chk_month:
#             return valid_month

#     for month in c_all_months:
#         if month == chk_month:
#             valid_month= True
#             break

#     return valid_month



# if __name__ == "__main__": 
#     get_months()



class Months(object):

    def __init__(self):
        self._start_months = [
            'January', 
            'March', 
            'May',
            'September', 
            'December',
        ]

        
        self._remove_list = [
            'May',
            'September',
            'October'   
        ]

        self._all_months = [
            'January',
            'February', 
            'March', 
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November', 
            'December'
        ]

    def valid_month(self,chk_month,input_list):
        valid_month= False
        for month in input_list:
            if month == chk_month:
                return valid_month

        for month in self._all_months:
            if month == chk_month:
                valid_month= True
                break

        return valid_month

class UpdateMonths(Months):

    def __init__(self):
        super().__init__()
        self._input_month = ""
        self._update_months = self._start_months

    def update_months(self):
        while True:
            try: 
                print("Current list of months")
                print("{}".format(self._update_months))
                self._input_month= input("Enter month: ")
                if not self.valid_month(self._input_month,self._update_months):
                    print("{0} is not a valid month name - try again".format(self._input_month))
                    continue
                x = self._update_months.append(self._input_month)
        
                if len(self._update_months) == 12:
                    print("Current list of months")
                    print("{}".format(self._update_months))
                    break
                else: 
                    print("Current month list is {} months".format(len(self._update_months)))
                    continue
            except Exception as e:
                print(e)
                continue
            
        
    def remove_months(self):
        for el in self._remove_list:
            print("Removing {} from the month list".format(el))
            self._update_months.remove(el)
    
    def final_print(self):
        print("Final list of months = {}".format(self._update_months))

um = UpdateMonths()
um.update_months()
um.remove_months()
um.final_print()




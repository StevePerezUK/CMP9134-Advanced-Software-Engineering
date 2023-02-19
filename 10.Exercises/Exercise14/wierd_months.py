#!/usr/bin/env python3

import sys

def get_months():

    start_months = [
        'January', 
        'March', 
        'May',
        'September', 
        'December',
    ]
    remove_list = [
     'May',
     'September',
     'October'   
    ]

    input_month = ""

    while True:
        print("Current list of months")
        print("{}".format(start_months))
        input_month= input("Enter month: ")
        if not valid_month(input_month,start_months):
            print("{0} is not a valid month name - try again".format(input_month))
            continue
        x = start_months.append(input_month)
        if len(start_months) == 12:
            print("Current list of months")
            print("{}".format(start_months))
            break
        else: 
            print("Current month list is {} months".format(len(start_months)))
            continue
    
    for el in remove_list:
        print("Removing {} from the month list".format(el))
        start_months.remove(el)
    
    print("Final list of months = {}".format(start_months))

def valid_month(chk_month,input_list):
    c_all_months = [
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

    valid_month= False
    for month in input_list:
        if month == chk_month:
            return valid_month

    for month in c_all_months:
        if month == chk_month:
            valid_month= True
            break

    return valid_month



if __name__ == "__main__": 
    get_months()

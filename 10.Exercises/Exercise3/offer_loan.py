#!/usr/bin/env python3

import sys

c_age_threshold = 21
c_income = 21000
c_recieved_loan = False
c_error_prompt = "This is an invalid input - Please enter Y/N at the prompt"

def get_customer_details():
    customer_details = {}
    l_age = input("Please enter your age: ")
    l_income = input("Please enter your annual income: ")
    while True:
        try:
            l_previous_loan = input("Please enter if you have had a previous loan (Y/N): ")
            if l_previous_loan == "N": 
                l_previous_loan = False
            elif l_previous_loan == "Y":
                l_previous_loan = True
            else:
                print(c_error_prompt)
                continue
        except:
            print(c_error_prompt)
            continue
        break
    customer_details.update({'age' : int(l_age)})
    customer_details.update({'income' : int(l_income)})
    customer_details.update({'prev_loan' : bool(l_previous_loan)})
    return customer_details

def check_loan_critera(details):
    application_approved = True
    if details['age'] < c_age_threshold:
        application_approved = False
    if details['income'] < c_income:
        application_approved = False    
    if details['prev_loan']:
        application_approved = False  

    return application_approved

def loan_apply():
    print("Hello and welcome to your loan application\n")
    customer_details = get_customer_details()
    if check_loan_critera(customer_details):
        print("\nYour loan has been approved\n")
        sys.exit(0)
    else:
        print("\nYour loan has not been approved, computer says no\n")
        sys.exit(1)

if __name__ == "__main__":
    loan_apply()

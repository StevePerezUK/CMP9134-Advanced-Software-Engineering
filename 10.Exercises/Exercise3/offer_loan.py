#!/usr/bin/env python3


####################
# Function version #
####################

# import sys

# c_age_threshold = 21
# c_income = 21000
# c_recieved_loan = False
# c_error_prompt = "This is an invalid input - Please enter Y/N at the prompt"

# def get_customer_details():
#     customer_details = {}
#     l_age = input("Please enter your age: ")
#     l_income = input("Please enter your annual income: ")
#     while True:
#         try:
#             l_previous_loan = input("Please enter if you have had a previous loan (Y/N): ")
#             if l_previous_loan == "N": 
#                 l_previous_loan = False
#             elif l_previous_loan == "Y":
#                 l_previous_loan = True
#             else:
#                 print(c_error_prompt)
#                 continue
#         except:
#             print(c_error_prompt)
#             continue
#         break
#     customer_details.update({'age' : int(l_age)})
#     customer_details.update({'income' : int(l_income)})
#     customer_details.update({'prev_loan' : bool(l_previous_loan)})
#     return customer_details

# def check_loan_critera(details):
#     application_approved = True
#     if details['age'] < c_age_threshold:
#         application_approved = False
#     if details['income'] < c_income:
#         application_approved = False    
#     if details['prev_loan']:
#         application_approved = False  

#     return application_approved

# def loan_apply():
#     print("Hello and welcome to your loan application\n")
#     customer_details = get_customer_details()
#     if check_loan_critera(customer_details):
#         print("\nYour loan has been approved\n")
#         sys.exit(0)
#     else:
#         print("\nYour loan has not been approved, computer says no\n")
#         sys.exit(1)

# if __name__ == "__main__":
#     loan_apply()

##################
# Object Version #
##################

class Application(object):

    def __init__(self):    
        self.c_age_threshold = 21
        self.c_income = 21000
        self.c_recieved_loan = False
        self.age = 0
        self.income = 0
        self.c_error_prompt = "This is an invalid input - Please enter Y/N at the prompt"


    def get_loan_inputs(self):
        print("Hello and welcome to your loan application\n")
        self.age = int(input("Please enter your age: "))
        self.income = int(input("Please enter your annual income: "))
        while True:
            try:
                self.previous_loan = input("Please enter if you have had a previous loan (Y/N): ")
                if self.previous_loan == "N": 
                    self.previous_loan = False
                elif self.previous_loan == "Y":
                    self.previous_loan = True
                else:
                    print(self.c_error_prompt)
                    continue
            except:
                print(self.c_error_prompt)
                continue
            break
    
        
class VerifyApplication(Application):
    
    def check_loan_criteria(self):
        self.get_loan_inputs()
        self.application_approved = True
        if self.age < self.c_age_threshold:
            self.application_approved = False
        if self.income < self.c_income:
            self.application_approved = False    
        if self.previous_loan:
            self.application_approved = False  
        return self.application_approved


class LoanApplication(VerifyApplication):

    def result(self):
        if self.check_loan_criteria():
            print("\nYour loan has been approved\n")
            return True
        else:
            print("\nYour loan has not been approved, computer says no\n")
            return False          
    



loan_application = LoanApplication()
loan_application.result()



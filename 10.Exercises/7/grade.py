#!/usr/bin/env python3

# def get_input():
#     print("Welcome to grade finder\n")
#     while True:
#         try:
#             score= int(input("Please enter the score for the exam - A number from 0 to 100: "))
#             if score < 0 or score > 100:
#                 print("Please enter a number between 0 and 100 {} is invalid".format(score))
#                 continue
#         except:
#             print("Please enter a number between 0 and 100")
#             continue
#         break
#     return score

# def mark_grade(mark):
#     if mark >= 70 and mark <= 100:
#         return "A"
#     elif mark >= 50 and mark < 70:
#         return "B"
#     elif mark >= 30 and mark < 50:
#         return "C"
#     elif mark >= 0 and mark < 30:
#         return "D"

# def show_grade():
#     score = get_input()
#     mark=  mark_grade(score)
#     print("The mark for a score of {0} is a {1}".format(score,mark))


# if __name__ == "__main__":
#     show_grade()

class GetInput(object):

    def __init__(self):
        self.score = 0

    def get_input(self):
        print("Welcome to grade finder\n")
        while True:
            try:
                self.score= int(input("Please enter the score for the exam - A number from 0 to 100: "))
                if self.score < 0 or self.score > 100:
                    print("Please enter a number between 0 and 100 {} is invalid".format(score))
                    raise Exception
            except Exception:
                print("Please enter a number between 0 and 100")
                continue
            break        

class CalculateGrade(GetInput):

    def __init__(self):
        super().__init__()
        self.get_input()
        self.grade = ""

    def mark_grade(self):
        if self.score >= 70 and self.score <= 100:
            self.grade = "A"
        elif self.score >= 50 and self.score < 70:
            self.grade = "B"
        elif self.score >= 30 and self.score < 50:
            self.grade = "C"
        elif self.score >= 0 and self.score < 30:
            self.grade = "D"


class ShowGrade(CalculateGrade):

    def __init__(self):
        super().__init__()
        self.mark_grade()

    def get_results(self):
        print("The mark for a score of {0} is a {1}".format(self.score,self.grade))


        
calc_grades = ShowGrade()
calc_grades.get_results()


#!/usr/bin/env python3

# import re

# def get_input():
#     letter= ""
#     while True:
#         try:
#             letter= input("Please enter a letter: ")
#             c_alphabet = re.search('[A-Za-z]',letter)
#             if not c_alphabet:
#                 print("Input is not a letter")
#                 continue
#             if len(letter) > 1:
#                 print("Please enter a single letter")
#                 continue
#             break
#         except: 
#             print("Please enter a single letter")
#             continue
#     return letter

# def classify_letter(letter):

#     is_vowel = re.search('[aeiouy]',letter.lower())
#     if is_vowel:
#         what_is_it = "vowel"
#     else:
#         what_is_it = "consonant"
    
#     print("The letter {0} is a {1}\n".format(letter,what_is_it))
    
# if __name__ == "__main__":
#     classify_letter(get_input())

class GetInput(object):

    def __init__(self):
        self._letter= ""
        self._alphabet = bool()

    def get_input(self):
        import re
        
        while True:
            try:
                self._letter= input("Please enter a letter: ")
                self._alphabet = re.search('[A-Za-z]',self._letter)
                if not self._alphabet:
                    raise Exception
                if len(self._letter) > 1:
                    print("Please enter a single letter")
                    raise Exception
            except Exception: 
                print("Please enter a single letter")
                continue
            break

class ClassifyLetter(GetInput):

    def __init__(self):
        super().__init__()
        self.get_input()
        self._vowel = bool()
        self._letter_type = ""

    def classify_letter(self):
        import re
        self._vowel = re.search('[aeiouy]',self._letter.lower())
        if self._vowel:
            self._letter_type = "vowel"
        else:
            self._letter_type = "consonant"

class GetLetterClassification(ClassifyLetter):

    def __init__(self):
        super().__init__()
        self.classify_letter()

    def print_class(self):
        print("The letter {0} is a {1}\n".format(self._letter,self._letter_type))


letter_type = GetLetterClassification()
letter_type.print_class()


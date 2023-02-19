#!/usr/bin/env python3

import re

def get_input():
    letter= ""
    while True:
        try:
            letter= input("Please enter a letter: ")
            c_alphabet = re.search('[A-Za-z]',letter)
            if not c_alphabet:
                print("Input is not a letter")
                continue
            if len(letter) > 1:
                print("Please enter a single letter")
                continue
            break
        except: 
            print("Please enter a single letter")
            continue
    return letter

def classify_letter(letter):

    is_vowel = re.search('[aeiouy]',letter.lower())
    if is_vowel:
        what_is_it = "vowel"
    else:
        what_is_it = "consonant"
    
    print("The letter {0} is a {1}\n".format(letter,what_is_it))
    
if __name__ == "__main__":
    classify_letter(get_input())

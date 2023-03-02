#!/usr/bin/env python3

# import random as r
# import sys

# def start_game():
#     c_word_list = [
#         'zoo',
#         'cat',
#         'dog',
#         'tree',
#         'house',
#         'keyboard',
#         'motorway',
#         'mouse',
#         'bird',
#         'keys'
#     ]

#     index = r.randint(0,9)
#     guess_word = c_word_list[index]
#     print("Welcome to hangman")
#     # - For debugging -- print("guess word = {}".format(guess_word))
#     display_list = []
#     init_display(display_list,guess_word)
#     guess_count = 0 
#     while True:
#         guess= input("\nPlease Guess a letter of the word: ")
#         if len(guess) > 1:
#             print("Only one letter at a time Cowboy")
#             continue
#         response = match_letter(guess,guess_word,display_list)
#         if not response['outcome']:
#             guess_count += 1
#         if guess_count == 7:
#             print("You lose Cowboy")
#             sys.exit(1)
#         display_list = response['display_list']
#         display_refresh(display_list)
#         winner=True
#         for el in display_list:
#             if str(el) == str("_"):
#                 winner=False       
        
#         if winner:
#             print("\n\nYou WIN Cowboy\n")
#             sys.exit(0) 

# def display_refresh(display_list):
#     for el in display_list:
#         print("{} ".format(el),end='')

# def match_letter(guess, guess_word,display_list):
#     match= guess_word.find(guess)
#     if match == -1:
#         return {'outcome': False,'display_list' : display_list}
#     display_list[match] = guess
#     while True:
#         match= guess_word.find(guess,match+1)
#         if match == -1:
#             return {'outcome' : True,'display_list' : display_list}
#         else:
#             display_list[match] = guess


# def init_display(display_list,guess_word):
#     print("Word = ",end='')
#     for el in range(0,len(guess_word)):
#         display_list.append('_')
#         print("_ ",end='')
#     print("")


# if __name__ == "__main__":
#     start_game()


import random as r
import sys


class InitGame(object):
    
    def __init__(self):
        self._word_list 


def start_game():
    c_word_list = [
        'zoo',
        'cat',
        'dog',
        'tree',
        'house',
        'keyboard',
        'motorway',
        'mouse',
        'bird',
        'keys'
    ]

    index = r.randint(0,9)
    guess_word = c_word_list[index]
    print("Welcome to hangman")
    # - For debugging -- print("guess word = {}".format(guess_word))
    display_list = []
    init_display(display_list,guess_word)
    guess_count = 0 
    while True:
        guess= input("\nPlease Guess a letter of the word: ")
        if len(guess) > 1:
            print("Only one letter at a time Cowboy")
            continue
        response = match_letter(guess,guess_word,display_list)
        if not response['outcome']:
            guess_count += 1
        if guess_count == 7:
            print("You lose Cowboy")
            sys.exit(1)
        display_list = response['display_list']
        display_refresh(display_list)
        winner=True
        for el in display_list:
            if str(el) == str("_"):
                winner=False       
        
        if winner:
            print("\n\nYou WIN Cowboy\n")
            sys.exit(0) 

def display_refresh(display_list):
    for el in display_list:
        print("{} ".format(el),end='')

def match_letter(guess, guess_word,display_list):
    match= guess_word.find(guess)
    if match == -1:
        return {'outcome': False,'display_list' : display_list}
    display_list[match] = guess
    while True:
        match= guess_word.find(guess,match+1)
        if match == -1:
            return {'outcome' : True,'display_list' : display_list}
        else:
            display_list[match] = guess


def init_display(display_list,guess_word):
    print("Word = ",end='')
    for el in range(0,len(guess_word)):
        display_list.append('_')
        print("_ ",end='')
    print("")






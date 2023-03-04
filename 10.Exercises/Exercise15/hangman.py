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


class InitGame(object):
    
    def __init__(self):
        self._word_list = [
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
        self.prompt_char = "_"
        self.guess_word = ""
        self.display_list = []
        self.max_guess_count = 7
        self.guess_count = 0
        self.select_word()
        self.init_list()

    def init_display(self):
        print("Welcome to Hangman") 
        print("Word = ",end='') 

    def init_list(self):
        len_word = len(self.guess_word) 
        for el in range(0,len_word):
            self.display_list.append(self.prompt_char)
    
    def print_prompt(self):
        import sys
        len_word = len(self.guess_word) 
        for el in range(0,int(len_word)):
            print("{0} ".format(self.display_list[el]),end='')
        print("")
 
    def select_word(self):
        import random as r
        index = r.randint(0,9)
        self.guess_word = self._word_list[index]
    
    
class GameInput(object):
 
    def get_guess(guess):
        while True:
            guess= input("\nPlease Guess a letter of the word: ")
            if len(guess) > 1:
                print("Only one letter at a time Cowboy")
                continue
            return guess

    def lose_message(self):
        print("{0}".format("You Lose Cowboy"))
        return
    
    def win_message(self):
        print("{0}".format("You WIN Cowboy!"))  
        return

class GameControl(InitGame,GameInput):

    def __init__(self):
        InitGame.__init__(self)

    def run_game(self):
        import sys
        #print("secret word = {}".format(self.guess_word))
        self.init_display()
        set_exit = False
        while True:
            self.print_prompt()
            if set_exit:
                sys.exit(0)
            guess= self.get_guess()
            return_dict = self.match_letter(guess,self.guess_word,self.display_list)
            if self.check_winner():
                self.win_message()
                set_exit = True          
            if not self.check_loser(return_dict):
                set_exit = True
        

    def check_loser(self,rd):
        if not rd['outcome']:
            self.guess_count += 1
        if self.guess_count == self.max_guess_count:
            self.lose_message()
            return False
        else:
            return True

    def check_winner(self):
        for el in self.display_list:
            if str(el) == str(self.prompt_char):
                return False
        return True

    def match_letter(self,guess, guess_word,display_list):
        match= guess_word.find(guess)
        if match == -1:
            return {'outcome' : False, 'display_list' : display_list }
        display_list[match] = guess
        while True:
            match= guess_word.find(guess,match+1)
            if match == -1:
                return {'outcome': True , 'display_list' : display_list }
            else:
                display_list[match] = guess


hangman = GameControl()
hangman.run_game()






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
        self._prompt_char = "_"
        self._guess_word = self.select_word()
        self._list_len = self.init_display(self._guess_word)
        self._display_list = self.init_list(self._guess_word)
        self._max_guess_count = 7
        self._guess_count = 0


    def init_display(self,guess_word):
        print("Welcome to Hangman") 
        print("Word = ",end='')
        return self.init_list(len(guess_word))
        
    def init_list(self,len):
        list = []
        for el in range(0,len):
            list.append(self._prompt_char)
        self.print_prompt(len)
        return list
    
    def print_prompt(self,len):
        for el in range(0,len):
            print("{0} ".format(el),end='')
        print("")

    def select_word(self):
        import random as r
        index = r.randint(0,9)
        return self._word_list[index]
    
    
class GameInput(object):
    
    def __init__():
        pass

    def get_guess(self):
        while True:
            guess= input("\nPlease Guess a letter of the word: ")
            if len(guess) > 1:
                print("Only one letter at a time Cowboy")
                continue
            return guess

    def lose_message():
        print("{0}".format("You Lose Cowboy"))

    def win_message():
        print("{0}".format("You WIN Cowboy!"))  


class GameControl(InitGame,GameInput):

    def __init__(self):
        super().__init__()
        self.run_game(self._guess_count,self._prompt_char)

    def run_game(self,guess_count,prompt_char):
        import sys
        while True:
            guess= self.get_guess()
            print(guess)
            sys.exit(1)
            return_dict = self.match_letter(guess,self._guess_word,self._display_list)
            if self.check_winner():
                self.win_message()
                break               
            if not self.check_loser(return_dict,guess_count,prompt_char):
                break
        

    def check_loser(self,rd,guess_count,prompt_char):
        if not rd['outcome']:
            guess_count += 1
        if guess_count == self._max_guess_count:
            self.lose_message()
            return False
        else:
            return True

    def check_winner(prompt_char,display_list):
        for el in display_list:
            if str(el) == str(prompt_char):
                return False
        return True

    def match_letter(guess, guess_word,display_list):
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






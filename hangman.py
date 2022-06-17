

import random
from re import M
from words import food_and_beverage, coding_temple, animals
import asciart
import os

    
def clear(): 
    os.system("clear||cls")


class Opening: 
    @staticmethod
    def heading(): 
        print(asciart.hangman_marquee)
        print(asciart.instructions)

class Word:
    def __init__(self, hangword :str): 
        self.hangword = hangword

    def display_word(self, guessed_letters):
        hidden_word = ""  
        for letter in self.hangword:
            if letter in guessed_letters:
                hidden_word += letter
            elif letter == " ": 
                hidden_word += "  "
            elif letter not in guessed_letters: 
                hidden_word += "_ "
        print(hidden_word)
            

class Session: 
    sessionword: Word 

    def __init__(self): 
        self.wrong_guesses = 7
        self.sessionword = None
        self.guessed_letters = [" "]
        self.wrong_guess_bank = []

    def get_word(self): 
        Opening.heading()
        category = input ("Pick a Category: \n[F]ood and Beverage \n[C]oding Temple \n[A]nimals \n ").lower()
        if category == "f": 
            self.sessionword = Word(random.choice(food_and_beverage))
            clear()
            Opening.heading()
        elif category == "c": 
            self.sessionword = Word(random.choice(coding_temple))
            clear()
            Opening.heading()
        elif category == "a": 
            self.sessionword = Word(random.choice(animals))
            clear()
            Opening.heading()
        else:
            clear()
            self.get_word()

    def guessing(self):  
        self.get_word()                   
        while self.wrong_guesses > 0:
            print(f"Here are your wrong guesses ->{self.wrong_guess_bank}\n")
            print(f"You have {self.wrong_guesses} guesses left before you die.\n---------------\n")
            self.sessionword.display_word(self.guessed_letters) #** This creates the disguised word.
            self.guess = input("---------------\nWhat is your guess?\n---------------\n")
            self.guessed_letters.append(self.guess)
            clear()
            if self.guess in self.sessionword.hangword: 
                self.correct_guess()
            if self.guess not in self.sessionword.hangword: 
                self.incorrect_guess()

    def correct_guess(self):
        if set(self.sessionword.hangword).issubset(self.guessed_letters):
            self.sessionword.display_word(self.guessed_letters)
            print(asciart.winner)
            self.wrong_guesses = 0
        else:
            Opening.heading()
            print("\n---------------\nNicely done!\n---------------")

    def incorrect_guess(self):
        self.wrong_guesses -= 1
        self.wrong_guess_bank.append(self.guess)
        if self.wrong_guesses== 0: 
            print(asciart.died)
        else:
            Opening.heading()
            print(f"\n---------------\nNope. [{self.guess}] isn't in your word")  
        


def game():
    Opening.heading()
    done = False
    while done != True:
        start_game = input("\n---------------\nWanna play? [y/n]\n---------------\n")
        if start_game == "n": 
            print("\n---------------\nOkay see ya later\n---------------\n")
            done = True
        if start_game == "y":
            clear()
            Session().guessing() 
            
#TODO: Maybe someday I'll get some Ascii characters to show a hangman
class Interface: 
    def __init__ (self):
        pass

game()
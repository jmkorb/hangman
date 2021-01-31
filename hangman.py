import random
import re
from getpass import getpass

def hangman(word):
    wrong = 0
    stages =[
            "__________          ",
            "|         |         ",
            "|         |         ",
            "|         O         ",
            "|        /|\        ",
            "|        / \        ",
    ]
    end = [
            "|                   ",
            "|___________________",
    ]
    rletters = list(word)
    board = ["_"] * len(word)
    if ' ' in rletters:
        while ' ' in rletters:
            space = rletters.index(' ')
            board[space] = ' '
            rletters[space] = '$'
    win = False
    print("Welcome to Hangman!\n{}".format(" ".join(board)))
    while wrong < len(stages) - 1:
        print("\n") 
        char = input("Guess a letter\n")
        up = char.upper()
        if char in rletters or up in rletters:
            while char in rletters:
                cind = rletters.index(char)
                board[cind] = char
                rletters[cind] = '$'
            while up in rletters:
                cind = rletters.index(up)
                board[cind] = up
                rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        if "_" not in board:
            print("\nYou win! You got {}".format(word))
            win = True
            break
        print("\n".join(stages[0: e]))
    if not win:
        for x in end:
            print(x)
        print("\nYou lose! It was {}".format(word))

use = getpass("Input your word, Player One: ")
hangman(use)

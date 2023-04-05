"""
This module contains the funtions that are useful for the game "Rock Paper Scissors"
"""
from random import choice


def introduce_game():
    """
    This is a very simple function which introduces the rock, paper, scissors game.
    """
    # Game Introduction.
    intro_str = "~" * 100
    intro_str += "\n\t\tWelcome to the game of Rock Paper Scissors!"
    intro_str += "\nHere’s how this game works: Rock beats scissors, "
    intro_str += "scissors beat paper, and paper beats rock.\n"
    intro_str += "You can use rock, paper, scissors to settle minor "
    intro_str += "decisions or simply play to pass the time.\n"
    intro_str += "~" * 100
    print(intro_str)


def full_form(acronym):
    """
    This function in an acronym for the rock paper scissors game where acronym
    'r' which stand for 'rock', p which stand for 'paper' and 
    's' which stand for 'scissors' and returns the full form of that acronym.
    """

    if acronym == 'r':
        full_form = 'rock'
    elif acronym == 'p':
        full_form = 'paper'
    elif acronym == 's':
        full_form = 'scissors'
    
    return full_form


def play():
    """
    The play function is the actual function used to play the game.
    """    
    # Prompting, and getting an input from the user.
    while True:
        prompt = "Enter 'r' for rock, 'p' for paper, and 's' for scissors: "
        user = input(prompt).lower()
        
        if user == 'r' or user == 'p' or user == 's':
            noun = full_form(user)
            print(f"You are '{noun}'. ", end='')
            break
        else:
            print("Please enter a correct input!")

    # Computer randomly making a choice between 'r', 'p', and 's'.
    computer = choice(['r', 'p', 's'])
    noun = full_form(computer)
    print(f"The computer is '{noun}'.")

    # Checking the conditions.
    if user == computer:
        print("\tIts tie!")
    elif (user == 'r' and computer == 's') or (user == 's' and computer == 'p') \
        or (user == 'p' and computer == 'r'):
        print('\tYou won!')
    else:
        print("\tYou lost!")
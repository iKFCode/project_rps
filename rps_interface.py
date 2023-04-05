from rps_functions import introduce_game, play

more = ''
while more.lower() != 'n':
    introduce_game()
    play()
    more = input("Would you like to play one more time (press 'n' to quit"
                 " or any other key to continue)? ")
print('See you next time!\n')
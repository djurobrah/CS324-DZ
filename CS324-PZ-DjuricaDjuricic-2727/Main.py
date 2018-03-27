from Game import *


def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    return letter


def playAgain():
    print('Play again? (yes or no)')
    return input().lower().startswith('y')


while True:
    game = Game(inputPlayerLetter())
    isPlaying = True;
    while isPlaying == True:
        isPlaying = game.nextMove()

    if not playAgain():
        break


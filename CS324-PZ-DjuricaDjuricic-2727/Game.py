import random
import os
import time

class Game:

    def __init__(self, playerLetter):
        self.playerLetter = playerLetter
        self.computerLetter = self.getOtherLetter(playerLetter)
        self.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.printNewGame()
        print("\n Player picked {}, computer is {}".format(self.playerLetter, self.computerLetter))
        self.printBoard(self.board)
        self.currentPlayer = self.whoGoesFirst()
        self.nextMove()

    def printNewGame(self):
        os.system('cls')
        print("""
         TicTacToeTicTacToeTicTacToeTicTacToeTicTacToeTicTacToeTicTacToeTicTacToe   
                                                                                    1 | 2 | 3
         -------------------------------NEW GAME-------------------------------     4 | 5 | 6
                                                                                    7 | 8 | 9
         TicTacToeTicTacToeTicTacToeTicTacToeTicTacToeTicTacToeTicTacToeTicTacToe   
        \
        """)

    def printBoard(self, board):
        print("""
             |     |     
          {}  |  {}  |  {}
        _____|_____|_____
             |     |     
          {}  |  {}  |  {}   
        _____|_____|_____
             |     |     
          {}  |  {}  |  {}  
             |     |
        """.format(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8]))

    def whoGoesFirst(self):
        if random.randint(0, 1) == 0:
            return "X"
        else:
            return "O"

    def getOtherLetter(self, letter):
        if(letter == "X"):
            return "O"
        else:
            return "X"

    def isFree(self, move):
        return not(self.board[move] == self.playerLetter or self.board[move] == self.computerLetter)

    def isWinner(self, letter):
        return\
            (
                self.board[0] == self.board[1] == self.board[2] == letter or
                self.board[3] == self.board[4] == self.board[5] == letter or
                self.board[6] == self.board[7] == self.board[8] == letter or
                self.board[0] == self.board[3] == self.board[6] == letter or
                self.board[1] == self.board[4] == self.board[7] == letter or
                self.board[2] == self.board[5] == self.board[8] == letter or
                self.board[0] == self.board[4] == self.board[8] == letter or
                self.board[2] == self.board[4] == self.board[6] == letter
            )


    def nextMove(self):
        if self.isTie():
            print("The game is a tie!")
            return False
        if self.currentPlayer == self.playerLetter:
            self.playerMove()
        else:
            time.sleep(1)
            print("Computer placed {} on {}.".format(self.computerLetter, self.computerMove() + 1))
        self.printBoard(self.board)
        if self.isWinner(self.currentPlayer):
            if(self.currentPlayer == self.playerLetter):
                print("Congrats! You've won.")
            else:
                print("The computer won!")
            return False
        self.currentPlayer = self.getOtherLetter(self.currentPlayer)
        return True


    def isTie(self):
        for i in range(len(self.board)):
            if(self.board[i] in "1 2 3 4 5 6 7 8 9".split()):
                return False
        return True

    def playerMove(self):
        move = 0
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isFree(int(move) - 1):
            print('What is your next move? (1-9)')
            move = input()
        self.board[int(move) - 1] = self.currentPlayer

    def computerMove(self):
        for i in range(0, 9):
            if self.isFree(i):
                self.board[i] = self.computerLetter
                if self.isWinner(self.computerLetter):
                    return i
                else:
                    self.board[i] = str(i+1)
        for i in range(0, 9):
            if self.isFree(i):
                self.board[i] = self.playerLetter
                if self.isWinner(self.playerLetter):
                    self.board[i] = self.computerLetter
                    return i
                else:
                    self.board[i] = str(i + 1)
        bestRandom = self.getRandomFrom([0, 2, 6, 8])
        if bestRandom != 100:
            self.board[bestRandom] = self.computerLetter
            return bestRandom
        else:
            if(self.isFree(4)):
                self.board[4] = self.computerLetter
                return 4
            else:
                bestRandom = self.getRandomFrom([1, 3, 5, 7])
                self.board[bestRandom] = self.computerLetter
                return bestRandom

    def getRandomFrom(self, list):
        playableMoves = []
        for i in range(len(list)):
            if self.isFree(list[i]):
                playableMoves.append(list[i])
        if len(playableMoves) == 0:
            return 100
        else:
            return random.choice(playableMoves)

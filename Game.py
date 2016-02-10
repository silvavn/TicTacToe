import sys, math, Players
from Boards import Board
from Players import MinimaxPlayer, HumanPlayer

class Game:
    def __init__(self, P1 = HumanPlayer("X"), P2 = HumanPlayer("O")):
        self.board = Board()
        self.isP1 = True
        self.finalState = False
        self.Player1 = P1
        self.Player2 = P2
        print "Game Started"
        
        while self.finalState == False:
            self.board.Print()
            if self.isP1:
                if self.Player1.Play(self.board):
                    self.isP1 = not self.isP1
            else:
                if self.Player2.Play(self.board):
                    self.isP1 = not self.isP1
                 
            self.finalState = self.board.WinCondition()
        
        self.board.Print()
        if self.finalState == "X":
            print "X wins!!!"
        elif self.finalState == "O":
            print "O wins!!!"
        else:
            print "Draw"


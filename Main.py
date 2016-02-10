import sys 
from Game import Game
from Players import HumanPlayer, MinimaxPlayer
print "teste"

P1 = None
P2 = None

for i in sys.argv:
    if i == "-m":
        if P1 == None:
            P1 = MinimaxPlayer("X")
        elif P2 == None:
            P2 = MinimaxPlayer("O")
    elif i == "-h":
        if P1 == None:
            P1 = HumanPlayer("X")
        elif P2 == None:
            P2 = HumanPlayer("O")
            
if P1 != None and P2 != None:
    g = Game(P1,P2)
else:
    g = Game()
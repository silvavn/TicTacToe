import sys
class Board:
    """May receive a Board to be copied. Creates an empty TicTacToe Board if no board is given"""
    def __init__(self, source = None):
        self.positions = {}
        self.lastX = -1
        self.lastY = -1
        
        if source == None:
            for i in range(0,3):
                for j in range(0,3):
                    self.positions[(i,j)] = "_";
        else:
            for p in source.positions:
                self.positions[p] = source.positions[p]
    
    """Receives a dictionary and sets to the Board"""
    def SetBoard(self, board):
        for b in board:
            self.positions[b] = board[b]
    
    """Returns a dictionary copy of the Board"""
    def GetCopy(self):
        r = {}
        for i in self.positions:
            r[i] = self.positions[i]
        return r
    
    '''Print the board in the console'''
    def Print(self):
        for i in range(0,3):
            for j in range(0,3):
                sys.stdout.write(self.positions[(i,j)] + "|" if j < 2 else self.positions[(i,j)] + "\n")
        print "\n"
    
    '''Plays in a defined position. Returns True if success, False unless'''
    def PlayAt(self, x, y, symbol):
        if x < 0 or x > 2:
            print "Invalid X position"
            return False
        elif y < 0 or y > 2:
            print "Invalid Y position"
            return False
        elif self.positions[(x,y)] != "_":
            print "Invalid position"
            return False
        else:
            self.positions[(x,y)] = symbol
            self.lastX = x
            self.lastY = y
            return True
    
    def CodifiedTable(self):
        r = {}
        for p in self.positions:
            r[p] = self.positions[p]
        return r
    
    '''Returns all available positions to be played in a list'''
    def AvailablePlays(self):
        r = []
        for p in self.positions:
            if self.positions[p] == "_":
                r.append(p)
        return r
    
    '''Verifies if someone won
    Returns:
    True -> draw
    False -> Not Finished
    Symbol [X,Y] -> someone won'''
    def WinCondition(self):
        for i in range(0,3):
            if self.positions[1,i] != "_" and self.positions[(2,i)] == self.positions[(0,i)] == self.positions[(1,i)]:
                return self.positions[(1,i)]
            elif self.positions[i,1] != "_" and self.positions[(i,2)] == self.positions[(i,0)] == self.positions[(i,1)]:
                return self.positions[(i,1)]
        if self.positions[1,1] != "_" and self.positions[(0,0)] == self.positions[(1,1)] == self.positions[(2,2)]:
            return self.positions[(1,1)]
        elif self.positions[1,1] != "_" and self.positions[(2,0)] == self.positions[(1,1)] == self.positions[(0,2)]:
            return self.positions[(1,1)]
        
        if len(self.AvailablePlays()) == 0:
            return True
        
        return False
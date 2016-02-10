from Boards import Board


class Player:
    def Play(self):
        raise NotImplementedError("Please Implement this method")

class MinimaxPlayer(Player):
    myID = ""
    enemyID = ""
    
    def __init__(self, ID):
        self.ID = ID
        MinimaxPlayer.myID = ID
        MinimaxPlayer.enemyID = "X" if ID == "O" else "O"
    
    def GenerateChild(self, board, symbol):
        r = []
        plays = board.AvailablePlays()
        for p in plays:
            b = Board(board)
            b.PlayAt(p[0],p[1], symbol)
            r.append(b)
        return r
    
    def Minimax(self, board, maxPlayer):
        value = board.WinCondition() 
        if value != False:
            if value == True:
                return 0
            else:
                return -1 if maxPlayer else 1
            
        
        if maxPlayer:
            _best = -float("inf")
            for b in self.GenerateChild(board, self.ID):
                v = self.Minimax(b, False)
                _best = max([_best,v])
            return _best
        else:
            _best = float("inf")
            for b in self.GenerateChild(board, MinimaxPlayer.enemyID):
                v = self.Minimax(b, True)
                _best = min([_best,v])
            return _best
        
    def Play(self, board):
        plays = self.GenerateChild(board, self.ID)
        
        
        weights = {}
        for p in plays:
            weights[p] = self.Minimax(p, False)

        _bestPlay = None
        _bestValue = -float("inf")
        for p in weights:
            if weights[p] > _bestValue or _bestPlay == None:
                _bestPlay = p
                _bestValue = weights[p]
        
        return board.PlayAt(_bestPlay.lastX, _bestPlay.lastY, self.ID)

class HumanPlayer(Player):
    def __init__(self, ID):
        self.ID = ID
        
    def Play(self, board):
        print "Player " + self.ID + " its your time" 
        x = int(raw_input("Line to be played"))
        y = int(raw_input("Row to be played"))
        
        return board.PlayAt(x,y,self.ID)
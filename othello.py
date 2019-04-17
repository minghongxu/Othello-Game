# Minghong Xu 81491461

class InvalidMoveError(Exception):
    '''Used when the move is invalid'''
    pass

class GameOverError(Exception):
    '''Used when move is made after game over'''
    pass

class GameState:
    def __init__(self, rownumber, colnumber, contents, turn) -> None:
        self.board = contents
        self.turn = turn
        self.bnumber = 2
        self.wnumber = 2

    def opposite_turn(self) -> str:
        if self.turn == 'B':
            self.turn = 'W'
        else:
            self.turn = 'B'
        return self.turn

    def neighbor(self, r, c):
        direction = []
        N = [[0, 1], [0, -1], [1, 1], [1, 0], [1, -1], [-1, 1], [-1, 0], [-1, -1]]
        for i in N:
            try:
                if self.board[r+i[0]][c+i[1]] != self.turn and self.board[r+i[0]][c+i[1]] != '.':
                    direction.append(i)
            except IndexError:
                pass
        return direction           

    def flip_over(self, r, c, direction):
        ava = False
        n = 0
        for direc in direction:
            if direc == [0, 1]:
                n = len(self.board)-c-1          
            elif direc == [0, -1]:
                n = c                           
            elif direc == [1, 1]:#right
                if len(self.board)-c >= len(self.board[0]) - r:
                    n = len(self.board[0]) - r -1
                else:
                    n = len(self.board)-c -1                              
            elif direc == [1, -1]:
                if len(self.board)-r-1>= c:
                    n = c
                else:
                    n = len(self.board)-r-1             
            elif direc == [1, 0]:
                n = len(self.board[0]) - r -1                          
            elif direc == [-1, 1]:
                if r >= len(self.board[0]) - c-1:
                    n = len(self.board[0]) - c-1
                else:
                    n = r               
            elif direc == [-1, 0]:
                n = r                           
            elif direc == [-1, -1]:
                if c >= r:
                    n = r
                else:
                    n = c
            for i in range(2,n+1):
                if self.board[r+i*direc[0]][c+i*direc[1]] == self.turn:
                    for j in range(i):#maybe change here
                        self.board[r+j*direc[0]][c+j*direc[1]] = self.turn
                    ava = True
                    break
        return ava
                       
                
    def move(self, r, c):
        self.bnumber = 0
        self.wnumber = 0
        turn = self.turn
        direction = self.neighbor(r, c)
        status = True
        if self.neighbor(r, c) == [] \
                or self.board[r][c] != '.' \
                or self.flip_over(r, c, direction) == False:
            status = False
        else:
            self.opposite_turn()
        
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 'B':
                    self.bnumber += 1
                elif self.board[i][j] == 'W':
                    self.wnumber += 1
        return status
        
    def winner(self, wincondition) -> str:
        winner = 'NONE'
        if wincondition == '<':
            if self.bnumber < self.wnumber:
                winner = 'B'
            elif self.bnumber > self.wnumber:
                winner = 'W'
        elif wincondition == '>':
            if self.bnumber < self.wnumber:
                winner = 'W'
            elif self.bnumber > self.wnumber:
                winner = 'B'
        return winner
    


#p = GameState(4, 4, 'B')
#p.move(1, 3)
#print(p.turn)
#r = 1
#c = 3
#print(p.neighbor(r, c))
#p.flip_over(r, c, p.neighbor(r, c))
#p.print_board()


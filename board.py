
''' 
board represent the game state which is initially set to [4,4,4,4,4,4,0,4,4,4,4,4,4,0]. 
You can pass any state into class Board(board) to generate a new instance.
'''
class Board:
    def __init__(self, board=None):
        if board is not None:
            self.board = board.board[:]
            self.reverse = board.reverse
            self.result = board.result
        else:
            self.board = [4,4,4,4,4,4,0,4,4,4,4,4,4,0] 
            #self.board = [1,1,1,1,1,1,0,1,1,1,1,1,1,0] 
            #self.board = [2,2,2,2,2,2,0,2,2,2,2,2,2,0]   
            #self.board = [3,3,3,3,3,3,0,3,3,3,3,3,3,0] 
            self.reverse = False
            self.result = None

    def __str__(self, *args, **kwargs):        
        return str(self.board)

    def __repr__(self, *args, **kwargs):
        return "board%s" % self.__str__()

    def find_possible_moves(self):  #finds all the available actions for the current player.
        temList = self.board[0:6]
        moveList = list()
        for i in range(0,6):
            if temList[i] !=0:
                moveList.append(i)
        return moveList

    def player_moves(self, n):  #pass and apply the action to the instance and return a boolean indicates whether the player gets another turn or not
        assert -1 < n < 6
        buffer = int(self.board[n])
        assert buffer > 0
        self.board[n] = 0
        while buffer > 0:
            n += 1
            if n == 13:
                n = -1
            else:
                self.board[n] += 1
                buffer -= 1
        if buffer == 0 and n == 6 and any(self.board[0:6]) == True:
            return True
        if buffer == 0 and 0 <= n <= 6 and self.board[n] == 1:
            opposite_position = len(self.board) - (n + 2)
            if self.board[opposite_position] != 0:
                self.board[6] += self.board[n] + self.board[opposite_position]
                self.board[n] = 0
                self.board[opposite_position] = 0
        return False


    def get_reverse_board(self):    #returns the opponents’ board towards the current player
        reverse_board = Board()
        reverse_board.board = self.board[7:] + self.board[:7]
        reverse_board.reverse = not self.reverse
        return reverse_board




    def terminate(self):    #detects if game ends or not
        if any(self.board[0:6]) == False:
            self.board[13] += sum(self.board[7:13])
            for i in range(7,13):
                self.board[i] = 0
            if self.board[6] > self.board[13]:
                self.result = "Player 1 wins!"
            elif self.board[6] < self.board[13]:
                self.result = "Player 2 wins!"
            else:
                self.result = "Draw"
            return True
        if any(self.board[7:13]) == False:
            self.board[6] += sum(self.board[0:6])
            for i in range(0,6):
                self.board[i] = 0
            if self.board[6] > self.board[13]:
                self.result = "Player 1 wins!"
            elif self.board[6] < self.board[13]:
                self.result = "Player 2 wins!"
            else:
                self.result = "Draw"
            return True
        if self.board[6] > 24:
            self.result = "Player 1 wins!"
            return True
        if self.board[13] > 24:
            self.result = "Player 2 wins!"
            return True
        return False
        


    def print(self):
        print("  "*2, end="")
        print(*["%2d" % i for i in [6,5,4,3,2,1]], sep=" ")
        print("    ------------------")
        print(" ", end="")
        print(*["%2d" % i for i in (self.board[7:14][::-1])], sep="|", end="|\n")
        print("  ----------------------")
        print("   |", end="")
        print(*["%2d" % i for i in (self.board[0:7])], sep="|")
        print("    ------------------")
        print("  "*2, end="")
        print(*["%2d" % i for i in [1,2,3,4,5,6]], sep=" ")




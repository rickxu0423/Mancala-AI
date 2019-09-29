from human_player import Human
from random_player import Random
from minimax_player import Minimax

class Agent:    #create player instance for both sides.
    def __init__(self, mode, name, board):
        self.mode = mode
        self.name = name
        self.board = board

    def __str__(self, *args, **kwargs):    
        return str(self.mode)
        
    def move(self): #returns the choice made by the specific agent
        if self.mode == "human":
            human = Human(self.name)
            choice = human.choice()
        if self.mode == "random":
            random = Random(self.name, self.board)
            choice = random.choice()
        if self.mode == "minimax":
            minimax = Minimax(self.name, self.board)
            choice = minimax.choice()
        if self.mode == "minimax_alpha_beta":
            minimax = Minimax(self.name, self.board)
            choice = minimax.choice_alpha_beta()
        return choice
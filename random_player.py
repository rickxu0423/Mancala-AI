import random

class Random:
    def __init__(self, name, board):
        self.name = name
        self.board = board
        

    def choice(self):
        option = self.board.find_possible_moves()
        choice = random.choice(option)
        #print(option)
        go_on = input("{}(random) move: {}".format(self.name, choice + 1))
        return choice

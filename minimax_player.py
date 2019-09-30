from board import Board
from time import time
import random

class Minimax:
    
    def __init__(self, name, board):
        self.name = name
        self.board = board
        self.counter = 0

    def minimax(self, board, turn, depth):
        if board.find_possible_moves(): #initialize best_move and deal with some exceptions
            best_move = random.choice(board.find_possible_moves())
        else: 
            best_move = 0
        if board.terminate() and turn == 1 or depth == 9 and turn == 1:
            return [self.heuristic_function(board, 1), best_move]
        elif board.terminate() and turn == -1 or depth == 9 and turn == -1:
            return [self.heuristic_function(board, -1), best_move]
        best_value = turn * -999
        for choice in board.find_possible_moves():  
            self.counter += 1
            board_copy = Board(board)   #create a new Board instance
            to_move = board_copy.player_moves(choice)
            if to_move: #if the player takes another turn
                value = self.minimax(board_copy, turn, depth+1)[0]
                if turn == 1:
                    if value > best_value:
                        best_value = value
                        if depth == 0:  #record the choice when depth == 0
                            best_move = choice
                    elif value == best_value:   # flip a coin to handle equivalent moves
                        coin = random.choice([0,1])
                        if coin == 1:
                            best_value = value
                            if depth == 0:
                                best_move = choice
                else:
                    if value < best_value:
                        best_value = value
                        if depth == 0:
                            best_move = choice
                    elif value == best_value:
                        coin = random.choice([0,1])
                        if coin == 1:
                            best_value = value
                            if depth == 0:
                                best_move = choice
            else:   #if the player gives the turn to its opponent
                board_copy = board_copy.get_reverse_board()
                value = self.minimax(board_copy, -1*turn, depth+1)[0]
                if turn == 1:
                    if value > best_value:
                        best_value = value
                        if depth == 0:
                            best_move = choice
                    elif value == best_value:
                        coin = random.choice([0,1])
                        if coin == 1:
                            best_value = value
                            if depth == 0:
                                best_move = choice
                else:
                    if value < best_value:
                        best_value = value
                        if depth == 0:
                            best_move = choice
                    elif value == best_value:
                        coin = random.choice([0,1])
                        if coin == 1:
                            best_value = value
                            if depth == 0:
                                best_move = choice
        return [best_value, best_move]    

    
    def minimax_alpha_beta(self, board, turn, depth, a, b):
        if board.find_possible_moves():
            best_move = random.choice(board.find_possible_moves())
        else: 
            best_move = 0
        if board.terminate() and turn == 1 or depth == 9 and turn == 1:
            return [self.heuristic_function(board, 1), best_move]
        elif board.terminate() and turn == -1 or depth == 9 and turn == -1:
            return [self.heuristic_function(board, -1), best_move]
        best_value = turn * -999
        for choice in board.find_possible_moves():  
            self.counter += 1
            board_copy = Board(board)
            to_move = board_copy.player_moves(choice)
            if to_move: #if the player takes another turn
                value = self.minimax_alpha_beta(board_copy, turn, depth+1, a, b)[0]
                if turn == 1:
                    if value > best_value:
                        best_value = value
                        if depth == 0:
                            best_move = choice
                        if best_value >= b:
                            return [best_value, best_move]
                        a = max(a, best_value)  #alpha_beta pruning
                    elif value == best_value:
                        coin = random.choice([0,1])
                        if coin == 1:
                            best_value = value
                            if depth == 0:
                                best_move = choice
                            if best_value >= b:
                                return [best_value, best_move]
                            a = max(a, best_value)
                else:
                    if value < best_value:
                        best_value = value
                        if depth == 0:
                            best_move = choice
                        if best_value <= a:
                            return [best_value, best_move]
                        b = min(b, best_value)  #alpha_beta pruning
                    elif value == best_value:
                        coin = random.choice([0,1])
                        if coin == 1:
                            best_value = value
                            if depth == 0:
                                best_move = choice
                            if best_value <= a:
                                return [best_value, best_move]
                            b = min(b, best_value)
            else:   ##if the player gives the turn to its opponent
                board_copy = board_copy.get_reverse_board()
                value = self.minimax_alpha_beta(board_copy, -1*turn, depth+1, a, b)[0]
                if turn == 1:
                    if value > best_value:
                        best_value = value
                        if depth == 0:
                            best_move = choice
                        if best_value >= b:
                            return [best_value, best_move]
                        a = max(a, best_value)
                    elif value == best_value:
                        coin = random.choice([0,1])
                        if coin == 1:
                            best_value = value
                            if depth == 0:
                                best_move = choice
                            if best_value >= b:
                                return [best_value, best_move]
                            a = max(a, best_value)
                else:
                    if value < best_value:
                        best_value = value
                        if depth == 0:
                            best_move = choice
                        if best_value <= a:
                            return [best_value, best_move]
                        b = min(b, best_value)
                    elif value == best_value:
                        coin = random.choice([0,1])
                        if coin == 1:
                            best_value = value
                            if depth == 0:
                                best_move = choice
                            if best_value <= a:
                                return [best_value, best_move]
                            b = min(b, best_value)
        return [best_value, best_move]  
        

    def heuristic_function(self, board, turn):  #returns the value equals to the score of player1 minus the score of player2
        if turn == 1:
            score = board.board[6] - board.board[13]
        if turn == -1:
            score = board.board[13] - board.board[6]
        return score
    
    def choice(self):
        board_copy = Board(self.board)
        print("Calculating best move...")
        t = time()  #store the current time

        if self.name == "player1":
            value, choice = self.minimax(board_copy, 1, 0)
        else: 
            value, choice = self.minimax(board_copy, -1, 0)
        print("Calculated in %.1fs" % (time() - t)) #get the calculation time
        print(self.counter, "states explored")
        go_on = input("{}(minimax) move: {}".format(self.name, choice + 1))
        return choice
    
    def choice_alpha_beta(self):
        board_copy = Board(self.board)
        print("Calculating best move...")
        t = time()

        if self.name == "player1":
            print()
            value, choice = self.minimax_alpha_beta(board_copy, 1, 0, -999, 999)
        else: 
            value, choice = self.minimax_alpha_beta(board_copy, -1, 0, -999, 999)
        print("Calculated in %.1fs" % (time() - t))
        print(self.counter, "states explored")
        go_on = input("{}(minimax_alpha_beta) move: {}".format(self.name, choice + 1))
        return choice

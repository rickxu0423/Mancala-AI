from game import Board
from time import time
import random

class Minimax:
    
    def __init__(self, name, board):
        self.name = name
        self.board = board

    def minimax(self, board, turn, depth):
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
            board_copy = Board(board)
            to_move = board_copy.player_moves(choice)
            if to_move:
                value = self.minimax(board_copy, turn, depth+1)[0]
                if turn == 1:
                    if value > best_value:
                        best_value = value
                        if depth == 0:
                            best_move = choice
                else:
                    if value < best_value:
                        best_value = value
                        if depth == 0:
                            best_move = choice
            else:
                board_copy = board_copy.get_reverse_board()
                value = self.minimax(board_copy, -1*turn, depth+1)[0]
                if turn == 1:
                    if value > best_value:
                        best_value = value
                        if depth == 0:
                            best_move = choice
                else:
                    if value < best_value:
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
            board_copy = Board(board)
            to_move = board_copy.player_moves(choice)
            if to_move:
                value = self.minimax_alpha_beta(board_copy, turn, depth+1, a, b)[0]
                if turn == 1:
                    if value > best_value:
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
            else:
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
                else:
                    if value < best_value:
                        best_value = value
                        if depth == 0:
                            best_move = choice
                        if best_value <= a:
                            return [best_value, best_move]
                        b = min(b, best_value)
        return [best_value, best_move]  
        

    def heuristic_function(self, board, turn):
        if turn == 1:
            score = board.board[6] - board.board[13]
        if turn == -1:
            score = board.board[13] - board.board[6]
        return score
    
    def choice(self):
        board_copy = Board(self.board)
        print("Calculating best move...")
        t = time()

        if self.name == "player1":
            value, choice = self.minimax(board_copy, 1, 0)
        else: 
            value, choice = self.minimax(board_copy, -1, 0)
        print("Calculated in %.1fs" % (time() - t))
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
        go_on = input("{}(minimax_alpha_beta) move: {}".format(self.name, choice + 1))
        return choice
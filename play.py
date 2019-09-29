from game import Board
from agent import Agent


def Player1_move(board, agent):
    to_move = True
    while to_move:
        choice = agent.move()
        try:
            to_move = board.player_moves(choice)
            board.print()
            agent.board = board
        except:
            print('Illegal move: ', choice + 1)
            continue
    return board

def Player2_move(board, agent):
    board = board.get_reverse_board()
    to_move = True
    while to_move:
        choice = agent.move()
        try:
            to_move = board.player_moves(choice)
            board.get_reverse_board().print()
            agent.board = board
        except:
            print('Illegal move: ', choice + 1)
            continue
    return board.get_reverse_board()

def Run_game():
    player1 = input('Select Player1 (human/random/minimax/minimax_alpha_beta): ')
    player2 = input('Select Player2 (human/random/minimax/minimax_alpha_beta): ')
    board = Board()
    board.print()
    while 1:
        agent = Agent(player1, "player1", board)
        board = Player1_move(board, agent)
        if board.terminate():
            board.print()
            print(board.result, "\nGame Ended")
            break
        agent = Agent(player2, "player2", board.get_reverse_board())
        board = Player2_move(board, agent)
        if board.terminate():
            board.print()
            print(board.result, "\nGame Ended")
            break

if __name__ == '__main__':
    Run_game()
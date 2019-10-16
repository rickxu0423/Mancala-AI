from board import Board
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
    print("1. human")
    print("2. random")
    print("3. minimax")
    print("4. minimax_alpha_beta")
    while 1:
        num1 = input('Select Player1 (1 to 4): ')
        if int(num1) == 1:
            player1 = "human"
            break
        elif int(num1) == 2:
            player1 = "random"
            break
        elif int(num1) == 3:
            player1 = "minimax"
            break
        elif int(num1) == 4:
            player1 = "minimax_alpha_beta"
            break
        else:
            print('Please input a number between 1 and 4!')

    while 1:
        num2 = input('Select Player2 (1 to 4): ')
        if int(num2) == 1:
            player1 = "human"
            break
        elif int(num2) == 2:
            player2 = "random"
            break
        elif int(num2) == 3:
            player2 = "minimax"
            break
        elif int(num2) == 4:
            player2 = "minimax_alpha_beta"
            break
        else:
            print('Please input a number between 1 and 4!')
    

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
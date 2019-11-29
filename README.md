CSC 442 Artificial Intelligence Course Project
======================================

Mancala AI
--------------

 __This project is about designing, implementing and evaluating an AI program that plays a game against human or computer opponents__

Brief Introduction:
---------------

Mancala is an ancient board game with many variants. This project is focusing on the popular (in the U.S) Kalah version.</br>
Briefly, this variant of Mancala is a two-player board agame where each player has a row of M pits where each pit is initially filled with K stones. For this project, we will use the standard setup of six pits each initally contining four stones. To each player's right on the board is a store. The objective for each player is to accumulate as many stones as possible into their own store.</br>

### Project Design
**board.py**: Describes the class Board() to create Mancala game instances when you start a new game or apply minimax algorithm. Inside the class:</br>
• board represent the game state which is initially set to [4,4,4,4,4,4,0,4,4,4,4,4,4,0]. You can pass any state into class Board(board) to generate a new instance</br>
• get_reverse_board() returns the opponents’ board towards the current player</br>
• find_possible_moves() finds all the available actions for the current player. Because
when opponent take turns, the board will be reversed, so the available action will always be board[0:6] if not zero</br>
• player_moves(action) pass and apply the action to the instance and return a boolean
indicates whether the player gets another turn or not</br>
• terminate() detects if game ends or not which will return true when there is no stones on either side of the board or either player gets more than 24 stones and print the result</br>
• print() is used to visualize the game board in order to have a better user experience
**agent.py**: Describes the class Agent() to create player instance for both sides</br>
• move() returns the choice made by the specific agent as user selected before the game
started which can be human, random, minimax or minimax_alpha_beta</br>
**human_player.py/random_player.py**: Describes the class Human()/Random() to create the
input prompt and return choice made by human/random players</br>
**minimax_player.py** Describes the class to create minimax and minimax_alpha_beta
searching instance and returns the best choice made by computer</br>
• minimax()/minimax_alpha_beta( ) pass ‘board’, ‘turn’ and ‘depth’ into itself. ‘board’ is the game state, ‘turn’ determine who is taking the turn and ‘depth’ indicates the current search depth. When the recursion comes to a terminate state or reaches the depth limit (which is **9**, you can change it if you want), the function returns an estimated utility value which created by **heuristic_function** which returns the value equals to **the score of player1 minus the score of player2**
**play.py**: Is the file to execute the game and deal with exceptions. Simply use a loop to deal with turn taking: If board.player_moves(action) == True: make another move, Else: give the turn to opponent and reverse the board</br>
 __Our minimax algorithm uses random to handle equivalent moves. (Flip a coin to determine whether to keep the move or not when encounter value == best_value situations)__

### How to Run the Game

Use command: **python3 play.py** to run the game.</br>
The first prompt asks you to type the mode for **player1** which will go first.</br> 
The second prompt asks you to type the mode for **player2** which will go after player 1.</br>

#### Game contains 4 types of player-mode:
    1. human
    2. random
    3. minimax
    4. minimax_alpha_beta

If you choose the player-mode other than human, every move chosen by the algorithm will be prompted and you should simply press **Enter** to go to the next turn.</br>
Although the algorithm is limited by its search depth to **9**, it is pretty hard for a human to beat a minimax or alpha_beta player.</br>
The estimated time for the first move of a minimax player is around **30s**, be patient, it will become faster and faster when the game goes.

**Please have fun with it!**

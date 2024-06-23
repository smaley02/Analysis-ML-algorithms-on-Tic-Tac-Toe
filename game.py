import random
from joblib import dump, load
import numpy as np

class TicTacToe:
    def __init__(self, model):
        self.board = []
        self.model = model

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def has_player_won(self, player):
        n = len(self.board)
        board_values = set()
        for i in range(n):
            for j in range(n):
                board_values.add(self.board[i][j])
            if board_values == {player}:
                return True
            else:
                board_values.clear()
        for i in range(n):
            for j in range(n):
                board_values.add(self.board[j][i])

            if board_values == {player}:
                return True
            else:
                board_values.clear()
        for i in range(n):
            board_values.add(self.board[i][i])
        if board_values == {player}:
            return True
        else:
            board_values.clear()
        board_values.add(self.board[0][2])
        board_values.add(self.board[1][1])
        board_values.add(self.board[2][0])
        if board_values == {player}:
            return True
        else:
            return False

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=' ')
            print()

    def start(self):
        self.create_board()
        player = 'X' if self.get_random_first_player() == 1 else 'O'
        game_over = False

        while not game_over:
            try:
                self.show_board()
                print(f'\nPlayer {player} turn')
                row, col = 0, 0
                # human player turn
                if player == "X":
                    row, col = list(
                        map(int, input(
                            'Enter row & column numbers to fix spot: ').split()))
                    print()
                # ai player turn
                else:
                    # get board as 2d array
                    ai_input = []
                    temp = []
                    for arr in self.board:
                        for i in range(len(arr)):
                            if arr[i] == "-":
                                temp.append(0)
                            # -1
                            elif arr[i] == "O":
                                temp.append(-1)
                            # +1
                            elif arr[i] == "X":
                                temp.append(1)
                    ai_input.append(temp)
                    ai_input = np.array(ai_input, dtype=np.float64)
                    regressor = load(self.model)
                    ai_output = regressor.predict(ai_input)
                    # get index with best probability of winning
                    curr_prob = -1
                    best_move = 0
                    for arr in ai_output:
                        for i in range(len(arr)):
                            if arr[i] > curr_prob:
                                best_move = i
                                curr_prob = arr[i]
                    # get row and cols from 0-based index
                    if best_move == 0:
                        ai_ind = "1 1"
                    elif best_move == 1:
                        ai_ind  = "1 2"
                    elif best_move == 2:
                        ai_ind = "1 3"
                    elif best_move == 3:
                        ai_ind = "2 1"
                    elif best_move == 4:
                        ai_ind = "2 2"
                    elif best_move == 5:
                        ai_ind = "2 3"
                    elif best_move == 6:
                        ai_ind = "3 1"
                    elif best_move == 7:
                        ai_ind = "3 2"
                    elif best_move == 8:
                        ai_ind = "3 3"
                    # print(f"{row} {col}")
                    row, col = list(map(int, ai_ind.split()))
                if col is None:
                    raise ValueError(
                        'not enough values to unpack (expected 2, got 1)')
                self.fix_spot(row - 1, col - 1, player)
                game_over = self.has_player_won(player)
                if game_over:
                    print(f'Player {player} wins the game!')
                    continue
                game_over = self.is_board_filled()
                if game_over:
                    print('Match Draw!')
                    continue
                player = self.swap_player_turn(player)
            except ValueError as err:
                print(err)
        print()
        self.show_board()


if __name__ == '__main__':
    chosen_model = int(input("CHOOSE MODEL:\n1. Multilayer Perceptron\n2. KNN\n3. Linear Regression\n"))
    if chosen_model == 1:
        path = 'mlp_reg.joblib'
    elif chosen_model == 2:
        path = 'knn_reg.joblib'
    elif chosen_model == 3:
        path = 'l_reg.joblib'
    tic_tac_toe = TicTacToe(path)
    tic_tac_toe.start()

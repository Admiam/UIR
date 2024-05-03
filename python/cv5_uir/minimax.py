import random
import numpy as np
import utils
from utils import Player


class MinimaxPlayer(Player):
    def __init__(self):
        super().__init__()

    def next_move(self, board: np.ndarray):
        """
        TODO: replace the random picking with minimax
        :param board: TicTacToe board as 2D ndarray. It contains +1, -1 and 0 values.
                        +1 - player 1
                        -1 - player 2
                         0 - empty
        :return: row, col - position of the next move in board: board[row][col]
        """
        print(self.MARKER)          # marker of the player is +1 or -1
        print(utils.WIN_STATE_LEN)  # winning sequence length
        print(board.shape)  # board size
        print(board)
        print(board[0][0])  # access value
        print(board[0, 0])  # access value
        print(board[:, 0])  # access column
        print(board[1:, :-1])   # sub-matrix

        game_end, winner = utils.evaluate_board_state(board)
        if game_end:
            if winner is None:
                print("DRAW")
            if winner == self.MARKER:
                print("I won")
            if winner == 1:
                print("+1 won")
            if winner == -1:
                print("-1 won")
        print("still playing")

        while True:
            row = random.choice(list(range(board.shape[0])))
            col = random.choice(list(range(board.shape[1])))
            if board[row][col] == 0:    # if random position is not taken
                return row, col

import numpy as np
import utils
from utils import Player

class MinimaxPlayer(Player):
    def __init__(self):
        super().__init__()
        self.first_move = True

    def next_move(self, board: np.ndarray):
        """
        TODO: replace the random picking with minimax
        :param board: TicTacToe board as 2D ndarray. It contains +1, -1 and 0 values.
                        +1 - player 1
                        -1 - player 2
                         0 - empty
        :return: row, col - position of the next move in board: board[row][col]
        """
        game_end, winner = utils.evaluate_board_state(board)
        if game_end:
            if winner is None:
                print("DRAW")
            elif winner == self.MARKER:
                print("I won")
            elif winner == 1:
                print("+1 won")
            elif winner == -1:
                print("-1 won")
            return None, None  # Game has ended, no move to make

        # if board is empty always play at (0, 0)
        if self.first_move and np.all(board == 0):
            self.first_move = False
            return 0, 0

        # implement Minimax algorithm to find the best move
        best_score = float('-inf')
        best_move = 0,0
        for row in range(board.shape[0]):
            for col in range(board.shape[1]):
                if board[row][col] == 0:
                    board[row][col] = self.MARKER
                    score = self.minimax(board, False)
                    board[row][col] = 0
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        return best_move

    def minimax(self, board, maximizing_player):
        game_end, winner = utils.evaluate_board_state(board)
        if game_end:
            if winner == self.MARKER:
                return 1
            elif winner == -self.MARKER:
                return -1
            else:
                return 0

        if maximizing_player:
            best_score = float('-inf')

            for row in range(board.shape[0]):
                for col in range(board.shape[1]):
                    if board[row][col] == 0:
                        board[row][col] = self.MARKER
                        score = self.minimax(board, False)
                        board[row][col] = 0
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            if np.all(board == 0):
                board[0][0] = self.MARKER
            for row in range(board.shape[0]):
                for col in range(board.shape[1]):
                    if board[row][col] == 0:
                        board[row][col] = -self.MARKER
                        score = self.minimax(board, True)
                        board[row][col] = 0  
                        best_score = min(score, best_score)
            return best_score

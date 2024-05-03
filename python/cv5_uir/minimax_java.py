import os
import random
import subprocess
import numpy as np

import utils
from utils import Player


class MinimaxPlayer(Player):
    def __init__(self, java_file="Minimax.java"):
        super().__init__()
        self.java_file = java_file
        subprocess.check_call(['javac', self.java_file])     # compile java file

    def next_move(self, board: np.ndarray):
        java_class, _ = os.path.splitext(self.java_file)
        output = subprocess.check_output(['java', java_class, str(utils.WIN_STATE_LEN), str(self.MARKER), str(board.tolist())]).decode('utf-8')
        splitindex = output.rindex(":")
        if splitindex > 0:
            print(output[:splitindex])
        res = output[splitindex + 1:]
        row, col = res.split(";")
        return int(row), int(col)

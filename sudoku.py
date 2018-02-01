from array  import array
from copy   import copy
from check  import Check
from heap   import Heap
from helper import Helper
from valid  import Valid

class Sudoku(Check, Valid, Helper):
    def __init__(self, buf):
        self.board = [0]
        self.stack = [array('I', map(int, list(buf)))]
        self.tried = 0

###############################################################################
# String Representation
###############################################################################

    def __str__(self):
        buf = '-' * 31 + '\n' + ' ' * 9 + "SUDOKU SOLVER" + ' ' * 10 + '\n'

        for row in range(9):
            if row % 3 == 0:
                buf += '-' * 31 + '\n'

            for col in range(9):
                if col % 3 == 0:
                    buf += '|'
                buf += ' ' + str(self.board[9 * row + col]) + ' '

            buf += "|\n"

        buf += '-' * 31 + '\n'

        return buf

###############################################################################
# Pop Next From Frontier
###############################################################################

    def popNext(self):
        self.board = self.stack.pop()
        self.tried += 1

        if 0 not in self.board and self.valid_all():
            return True

###############################################################################
# (1) Backtracking with Validation
###############################################################################

    def expandV(self):
        if self.valid_all():
            index = self.board.index(0)

            for num in list(range(1, 10)):
                child = copy(self.board)
                child[index] = num

                self.stack.append(child)

###############################################################################
# (2) Backtracking with Forward-Checking
###############################################################################

    def expandFC(self):
        index = self.board.index(0)

        for num in list(range(1, 10)):
            if self.check_all(num, index):
                child = copy(self.board)
                child[index] = num

                self.stack.append(child)

###############################################################################
# (3) Backtracking with Forward-Checking & Minimum-Remaining-Value Heuristic
###############################################################################

    def expandMRV(self):
        indices = [i for i, v in enumerate(self.board) if not v]
        minHeap = Heap([], len)

        for index in indices:
            children = []

            for num in list(range(1, 10)):
                if self.check_all(num, index):
                    child = copy(self.board)
                    child[index] = num

                    children.append(child)

            minHeap.insert(children)

        for child in minHeap.delete():
            self.stack.append(child)

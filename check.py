from blocks import BLOCKS
from helper import Helper

###############################################################################
# Mixin for Forward-Checking
###############################################################################

class Check:
    def check_all(self, num, index):
        return \
            self.check_row(num, index) and \
            self.check_col(num, index) and \
            self.check_blk(num, index)

    def check_row(self, num, index):
        coord = self.i2c(index)

        for col in range(9):
            if self.board[self.c2i([coord[0], col])] == num:
                return False
        return True

    def check_col(self, num, index):
        coord = self.i2c(index)

        for row in range(9):
            if self.board[self.c2i([row, coord[1]])] == num:
                return False

        return True

    def check_blk(self, num, index):
        coord = self.i2c(index)

        rows, cols = [], []

        for block in BLOCKS:
            if coord[0] in block:
                rows = block
            if coord[1] in block:
                cols = block

        for row in rows:
            for col in cols:
                if self.board[self.c2i([row, col])] == num:
                    return False
        return True

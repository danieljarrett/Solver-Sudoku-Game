from blocks import BLOCKS
from helper import Helper

###############################################################################
# Mixin for Validation
###############################################################################

class Valid:
    def valid_all(self):
        return \
            self.valid_row() and \
            self.valid_col() and \
            self.valid_blk()

    def valid_row(self):
        for row in range(9):
            list = [self.board[self.c2i([row, col])] \
                for col in range(9) if self.board[self.c2i([row, col])]]

            if len(list) != len(set(list)):
                return False

        return True

    def valid_col(self):
        for col in range(9):
            list = [self.board[self.c2i([row, col])] \
                for row in range(9) if self.board[self.c2i([row, col])]]

            if len(list) != len(set(list)):
                return False

        return True

    def valid_blk(self):
        for blk_row in range(3):
            for blk_col in range(3):
                list = []

                for row in range(3):
                    for col in range(3):
                        if self.board[self.c2i([  \
                            BLOCKS[blk_row][row], \
                            BLOCKS[blk_col][col]  \
                        ])]:
                            list.append(self.board[self.c2i([ \
                                BLOCKS[blk_row][row],         \
                                BLOCKS[blk_col][col]          \
                            ])])

                if len(list) != len(set(list)):
                    return False

        return True

from sudoku import Sudoku
from time   import sleep

###############################################################################
# Animated Solver
###############################################################################

# NOTE: The animation has been purposefully slowed down for demonstrative
# purposes. You can change the sleep(0.01) function to adjust the speed.

# (1) Basic Difficulty
basic   = "105802000090076405200400819019007306762083090000061050007600030430020501600308900"

# (2) Medium Difficulty
medium  = "000000760000008005400260000010050004700080530300006100000001000087000003640035871"

# (3) Extreme Difficulty
extreme = "020000000700502000008070405902010008030060079040000300000100000010006002000098700"

# Illegal Board
illegal = "220000000700502000008070405902010008030060079040000300000100000010006002000098700"

# Empty Board
empty   = "000000000000000000000000000000000000000000000000000000000000000000000000000000000"

# ------------------------------------------- #
# CHANGE THIS VALUE TO PLAY WITH THE EXAMPLES #
# ------------------------------------------- #
#                                             #
buf = extreme # <<<------
#                                             #
# ------------------------------------------- #

sudoku = Sudoku(buf)

try:
    while (0 in sudoku.board or not sudoku.valid_all()):
        if sudoku.popNext():
            break

        sudoku.expandMRV()

        print(chr(27) + '[2J')
        print(sudoku)
        print("Total searched:\n\n" + str(sudoku.tried) + \
            ", using sudoku.expandMRV()" + '\n')

        sleep(0.01)

except IndexError:
    print("INVALID INPUT: this initial board is unsolvable.")

    quit()

print(chr(27) + '[2J')
print(sudoku)
print("Total searched:\n\n" + str(sudoku.tried) + \
    ", using sudoku.expandMRV()" + '\n')

from sudoku import Sudoku

###############################################################################
# Driver & Examples
###############################################################################

# (1) Basic Difficulty
basic   = "105802000090076405200400819019007306762083090000061050007600030430020501600308900"

# (2) Medium Difficulty
medium  = "020000000700502000008070405902010008030060079040000300000100000010006002000098700"

# (3) Extreme Difficulty
extreme = "000000760000008005400260000010050004700080530300006100000001000087000003640035871"

# Illegal Board
illegal = "220000000700502000008070405902010008030060079040000300000100000010006002000098700"

# Empty Board
empty   = "000000000000000000000000000000000000000000000000000000000000000000000000000000000"

# ------------------------------------------- #
# CHANGE THIS VALUE TO PLAY WITH THE EXAMPLES #
# ------------------------------------------- #
#                                             #
buf = basic # <<<------
#                                             #
# ------------------------------------------- #

for exp in ["sudoku.expandV()", "sudoku.expandFC()", "sudoku.expandMRV()"]:
    sudoku = Sudoku(buf)

    try:
        while (0 in sudoku.board or not sudoku.valid_all()):
            if sudoku.popNext():
                break

            eval(exp)

    except IndexError:
        print("INVALID INPUT: this initial board is unsolvable.")

        quit()

    print(sudoku)
    print("Total searched:\n\n" + str(sudoku.tried) + ", using " + exp + '\n')

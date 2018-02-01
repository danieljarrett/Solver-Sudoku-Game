###############################################################################
# Mixin for Coordinate Helpers
###############################################################################

class Helper:
    def i2c(self, index):
        return divmod(index, 9)

    def c2i(self, coord):
        return coord[0] * 9 + coord[1]

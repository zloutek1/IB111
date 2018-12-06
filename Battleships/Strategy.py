from random import shuffle, choice
from config import *


class Strategy:
    def __init__(self, rows=ROWS, columns=COLS):
        self.rows = rows
        self.columns = columns

    def nextCoords(self):
        "return coordinates in format (y, x)"
        raise NotImplementedError

    def didHitShip(self, *, at):
        "triggered when player did hit ship"

    def didSinkShip(self, *, at):
        "triggered when player did sink ship"

    def didMissShip(self, *, at):
        "triggered when player missed ships"

    def reset(self):
        "reset to default values"
        self.__init__(self.rows, self.columns)

    @staticmethod
    def getSurroundingTilesAround(tile):
        return (
            (tile[0] - 1, tile[1]),  # UP
            (tile[0] + 1, tile[1]),  # DOWN
            (tile[0], tile[1] - 1),  # LEFT
            (tile[0], tile[1] + 1)   # RIGHT
        )

    @property
    def name(self):
        return self.__class__.__name__

    def __str__(self):
        return f"Strategy {self.__class__.__name__}"

    def __repr__(self):
        return f"Strategy({self.__class__.__name__})"


class Randomized(Strategy):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.availableOptions = [(row, column) for row in range(self.rows) for column in range(self.columns)]
        shuffle(self.availableOptions)

    def nextCoords(self):
        while True:
            yield self.availableOptions.pop()


class TopLeft(Strategy):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.row = 0
        self.column = -1

    def nextCoords(self):
        while True:
            self.column += 1
            if self.column > self.columns - 1:
                self.column = 0
                self.row += 1

            yield (self.row, self.column)


class RandomThenSink(Strategy):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.availableOptions = [(row, column) for row in range(self.rows) for column in range(self.columns)]
        shuffle(self.availableOptions)

        self.didLocateShip = False
        self.locatedShip = None

    def nextCoords(self):
        while True:
            if not self.didLocateShip or self.locatedShip is None:
                yield self.availableOptions.pop()
                continue

            neighbourTiles = self.getSurroundingTilesAround(self.locatedShip)
            neighbourTiles = tuple(filter(lambda tile: tile in self.availableOptions, neighbourTiles))

            if len(neighbourTiles) == 0:
                self.didLocateShip = False
                yield self.availableOptions.pop()
                continue

            nextTile = choice(neighbourTiles)
            self.availableOptions.remove(nextTile)

            yield nextTile

    def didHitShip(self, *, at):
        self.didLocateShip = True
        self.locatedShip = at

    def didSinkShip(self, *, at):
        self.didLocateShip = False
        self.locatedShip = None


class MiddleOut(Strategy):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.availableOptions = [(row, column) for row in range(self.rows) for column in range(self.columns)]

        self.row = self.rows // 2
        self.column = self.columns // 2

    def nextCoords(self):
        yield self.availableOptions[self.row * ROWS + self.column]

        n = 0
        counter = 0
        while True:
            try:
                if counter % 2 == 0:
                    # move right-down
                    for i in range(n):
                        self.column += 1
                        yield self.availableOptions[self.row * ROWS + self.column]

                    for i in range(n):
                        self.row += 1
                        yield self.availableOptions[self.row * ROWS + self.column]

                    n += 1
                else:
                    # move left-up
                    for i in range(n):
                        self.column -= 1
                        yield self.availableOptions[self.row * ROWS + self.column]

                    for i in range(n):
                        self.row -= 1
                        yield self.availableOptions[self.row * ROWS + self.column]

                    n += 1

                counter += 1
            except IndexError:
                break

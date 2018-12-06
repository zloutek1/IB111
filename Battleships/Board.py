from config import *
from typing import Tuple
from random import randrange, choice
from pprint import pformat
import numpy as np

from Ship import *


class Board:
    def __init__(self, ofWidth=ROWS, ofHeight=COLS):
        self._array = np.array([[0] * ofWidth] * ofHeight)
        self.lastHitShip = None

        self.ships = [
            Ship("Carrier", length=5),
            Ship("Battleship", length=4),
            Ship("Cruiser", length=3),
            Ship("Submarine", length=3),
            Ship("Destroyer", length=2)
        ]

        self.placeShips()

    def placeShips(self):
        for i, ship in enumerate(self.ships):
            ship.id = i + 1

            orientation = choice(("vertical", "horizontal"))

            if orientation == "vertical":
                self._placeShipVertical(ship)

            elif orientation == "horizontal":
                self._placeShipHorisontal(ship)

    def _placeShipVertical(self, ship, limit_counter=0):
        x = randrange(COLS - ship.length)
        y = randrange(ROWS)

        """
        spaceSelected = self._array[y, x:(x + ship.length)]
        isSpaceUnoccupied = (len(set(spaceSelected)) == 1 and
                             set(spaceSelected) == {0})
        """

        surroundingSpace = self._array[y - 1:y + 2, x - 1:(x + ship.length) + 1]
        areSurroundingsUnoccupied = (len(set(surroundingSpace.flatten())) == 1 and
                                     set(surroundingSpace.flatten()) == {0})

        if areSurroundingsUnoccupied:
            self._array[y, x:(x + ship.length)] = ship.id
            ship.placement = [(y, x + i) for i in range(ship.length)]
            return True

        else:
            if limit_counter <= 100:
                return self._placeShipVertical(ship, limit_counter + 1)

            return False

    def _placeShipHorisontal(self, ship, limit_counter=0):
        x = randrange(COLS)
        y = randrange(ROWS - ship.length)

        """
        spaceSelected = self._array[y:(y + ship.length), x]
        isSpaceUnoccupied = (len(set(spaceSelected)) == 1 and
                             set(spaceSelected) == {0})
        """

        surroundingSpace = self._array[y - 1:(y + ship.length) + 1, x - 1:x + 2]
        areSurroundingsUnoccupied = (len(set(surroundingSpace.flatten())) == 1 and
                                     set(surroundingSpace.flatten()) == {0})

        if areSurroundingsUnoccupied:
            self._array[y:(y + ship.length), x] = ship.id
            ship.placement = [(y + i, x) for i in range(ship.length)]
            return True

        else:
            if limit_counter <= 100:
                return self._placeShipHorisontal(ship, limit_counter + 1)

            return False

    def didHitShip(self, *, at: Tuple[int, int]):
        coords = at

        for ship in self.ships:
            if ship.wasHit(at=coords):
                self.lastHitShip = ship
                return True
        return False

    def getHitStip(self):
        return self.lastHitShip

    def __getitem__(self, key):
        return self._array[key]

    def __setitem__(self, key, value):
        self._array[key] = value

    def __str__(self):
        return pformat(self._array)

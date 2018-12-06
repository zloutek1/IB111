from config import *
from typing import Tuple
import numpy as np

from Board import *


class Score:
    def __init__(self):
        self.hit = 0
        self.missed = 0
        self.shipsSank = 0

        self.wonTimes = 0
        self.gamesPlayed = 0

    def __add__(self, another):
        new_score = Score()
        new_score.hit = self.hit + another.hit
        new_score.missed = self.missed + another.missed
        new_score.shipsSank = self.shipsSank + another.shipsSank
        new_score.wonTimes = self.wonTimes + another.wonTimes
        new_score.gamesPlayed = self.gamesPlayed + another.gamesPlayed
        return new_score

    def __str__(self):
        return f"Score(hit={self.hit}, missed={self.missed}, shipsSank={self.shipsSank})"

    def __repr__(self):
        return f"Score(hit={self.hit}, missed={self.missed}, shipsSank={self.shipsSank})"


class Player:
    def __init__(self, strategy):
        self.board = Board()
        self.strategy = strategy
        self.score = Score()

        self.myShipHitMap = np.array([[0] * COLS] * ROWS)
        self.attackCoords = self.strategy.nextCoords()

    def reset(self):
        self.strategy.reset()
        self.__init__(self.strategy)

    def attack(self, enemy, *, at: Tuple[int, int] = None):
        coords = at

        """
        attack the other player,
        update board with values:

            0 is unused
            1 is missed
            2 is hit
            3 is sank
        """

        if coords is None:
            coords = next(self.attackCoords)

        if enemy.board.didHitShip(at=coords):
            self.score.hit += 1
            self.strategy.didHitShip(at=coords)
            enemy.myShipHitMap[coords] = 2

            hitShip = enemy.board.getHitStip()
            if hitShip.wasSank():
                self.score.shipsSank += 1
                self.strategy.didSinkShip(at=coords)

                for coord in hitShip.placement:
                    enemy.myShipHitMap[coord] = 3

        else:
            self.score.missed += 1
            self.strategy.didMissShip(at=coords)
            enemy.myShipHitMap[coords] = 1

    def hasWon(self, *, against):
        enemy = against

        return False not in map(lambda ship: ship.wasSank(), enemy.board.ships)

    def visualise(self):
        import tkinter as tk

        root = tk.Tk()
        canvas = tk.Canvas(root, width=600, height=300)
        canvas.pack()

        canvas.create_text(300, 15, text=self.strategy.__class__.__name__, font="Arial 25")

        def drawBoard(startX, startY, WIDTH, HEIGHT, rows=ROWS, cols=COLS, data=None, translucent=False):
            canvas.create_rectangle(startX, startY, startX + WIDTH, startY + HEIGHT)

            x, y = startX, startY
            for i in range(rows):
                for j in range(cols):
                    if data is not None and data[i][j] != 0:
                        if translucent:
                            canvas.create_rectangle(x, y, x + WIDTH / cols, y + HEIGHT / rows, fill='gray', stipple='gray50')
                        else:
                            canvas.create_rectangle(x, y, x + WIDTH / cols, y + HEIGHT / rows, fill='yellow')
                    else:
                        canvas.create_rectangle(x, y, x + WIDTH / cols, y + HEIGHT / rows)
                    x += WIDTH / cols
                x = startX
                y += HEIGHT / rows

        drawBoard(200, 50, 200, 200, rows=ROWS, cols=COLS, data=self.board)
        drawBoard(200, 50, 200, 200, rows=ROWS, cols=COLS, data=self.myShipHitMap, translucent=True)

        root.mainloop()

    def __str__(self):
        return f"Player with {self.strategy}"

    def __repr__(self):
        return f"Player({self.strategy})"

from config import *
from typing import Tuple


class Ship:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.id = None

        self.placement = []
        self.hitParts = []

    def wasHit(self, at: Tuple[int, int]):
        coords = at

        if coords in self.placement:
            self.hitParts.append(self.placement[self.placement.index(coords)])
            return True
        return False

    def wasSank(self):
        return len(self.hitParts) == self.length

    def __str__(self):
        return f"{self.name} of length {self.length}"

    def __repr__(self):
        return f"Ship(length={self.length}, sank={self.wasSank()})"

from random import randrange
from math import ceil


def mprint(mapa):
    for row in mapa:
        print("".join(row))


def createMap(ROWS, COLS):
    mapa = [["#" if 0 in (row, col) or (ROWS - 1) in (row, col) else "."
             for col in range(COLS)] for row in range(ROWS)]

    mapa[0][1] = 'S'
    mapa[ROWS - 1][COLS - 2] = 'E'

    return mapa


def getIndex(num):
    if ((num - 1) / 2) % 2 == 0:
        return num // 2
    else:
        return round(num / 2)


def divide(mapa, direction='vertical'):
    width, height = len(mapa[0]), len(mapa)

    if (direction == 'vertical' and height <= 3) or (direction == 'horizontal' and width <= 3):
        return mapa

    division_index = (getIndex(width)
                      if direction == 'vertical' else
                      getIndex(height))

    doorway_index = (randrange(1, height, 2)
                     if direction == 'vertical' else
                     randrange(1, width, 2))

    if direction == 'vertical':
        for i in range(height):
            new_value = "." if i == doorway_index else "#"
            mapa[i][division_index] = new_value

        Lmap = [row[:division_index + 1][:] for row in mapa]
        Rmap = [row[division_index:][:] for row in mapa]

        Lmap = divide(Lmap, direction='horizontal')
        Rmap = divide(Rmap, direction='horizontal')

        mapa = [Lmap + Rmap[1:] for Lmap, Rmap in zip(Lmap, Rmap)]

    else:
        for i in range(width):
            new_value = "." if i == doorway_index else "#"
            mapa[division_index][i] = new_value

        for i in range(width):
            if i == doorway_index:
                mapa[division_index][i] = '.'
            else:
                mapa[division_index][i] = '#'

        Lmap = mapa[:division_index + 1][:]
        Rmap = mapa[division_index:][:]

        Lmap = divide(Lmap, direction='vertical')
        Rmap = divide(Rmap, direction='vertical')

        mapa = Lmap + Rmap[1:]

    return mapa


def generateMaze(ROWS, COLS):
    ROWS = ROWS + 1 if ROWS % 2 == 0 else ROWS
    COLS = COLS + 1 if COLS % 2 == 0 else COLS

    mapa = createMap(ROWS, COLS)
    maze = divide(mapa)
    return maze


if __name__ == '__main__':
    ROWS = 7
    COLS = 7
    maze = generateMaze(ROWS, COLS)
    mprint(maze)

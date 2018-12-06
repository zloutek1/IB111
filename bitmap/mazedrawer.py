import mazemaker
import mazereader
import mazepathfind
from PIL import Image
from random import choice
from math import ceil, log


def getWhiteIndex():
    whiteIndexes = [(i + 1, i) for i in range(3)] + [(i, i + 1) for i in range(3)]
    return choice(whiteIndexes)


def getBlackIndex():
    whiteIndexes = [(3 - (i + 1), i) for i in range(3)] + [(i, 3 - (i + 1)) for i in range(3)]
    return choice(whiteIndexes)


def drawMaze(maze, steps=[], tileSize=128, save=False, savePath="maze.png"):
    ROWS = len(maze)
    COLS = len(maze[0])

    scale = tileSize / 128
    floorImage = Image.open(tile_path)
    floorWidth, floorHeight = floorImage.size[0] // 4, floorImage.size[1] // 4

    pathMarkerImage = Image.open(marker_path)
    pathMarkerImage.thumbnail((tileSize, tileSize))

    mazeImage = Image.new('RGBA', (int(COLS * floorWidth * scale), int(ROWS * floorHeight * scale)))

    x, y = 0, 0
    for i, row in enumerate(maze):
        for j, tile in enumerate(row):
            if tile == '.' and abs(j - i) % 2 == 0:
                # white tile
                whiteX, whiteY = getWhiteIndex()
                whiteTile = floorImage.crop((whiteX * floorWidth, whiteY * floorHeight, (whiteX + 1) * floorWidth, (whiteY + 1) * floorHeight))
                whiteTile.thumbnail((tileSize, tileSize))
                mazeImage.paste(whiteTile, (x, y, x + whiteTile.size[0], y + whiteTile.size[1]))

            elif tile == '.' and abs(j - i) % 2 != 0:
                # black tile
                blackX, blackY = getBlackIndex()
                blackTile = floorImage.crop((blackX * floorWidth, blackY * floorHeight, (blackX + 1) * floorWidth, (blackY + 1) * floorHeight))
                blackTile.thumbnail((tileSize, tileSize))
                mazeImage.paste(blackTile, (x, y, x + blackTile.size[0], y + blackTile.size[1]))

            else:
                mazeImage.paste((0, 0, 0), (x, y, x + tileSize, y + tileSize))

            if (j, i) in steps:
                # correct solution
                mazeImage.paste(pathMarkerImage, (x, y, x + pathMarkerImage.size[0], y + pathMarkerImage.size[1]))

            x += int(floorWidth * scale)

        x = 0
        y += int(floorHeight * scale)

    mazeImage.show()
    if save:
        mazeImage.save(savePath)


if __name__ == '__main__':
    ROWS = 10
    COLS = 10

    ROWS = ROWS + 1 if ROWS % 2 == 0 else ROWS
    COLS = COLS + 1 if COLS % 2 == 0 else COLS

    mazeImage = "maze.png"
    tile_path = "floor.png"
    marker_path = "gem_trans_static.png"

    maze = mazemaker.generateMaze(ROWS, COLS)
    drawMaze(maze, [], tileSize=64, save=True)

    maze_from_img = mazereader.generateMaze(path=mazeImage)

    steps = mazepathfind.findPath(maze_from_img, endPos=mazepathfind.Vector(COLS - 2, ROWS - 1))

    drawMaze(maze, steps, tileSize=64, save=True, savePath="solved.png")
    # loadMaze()

from PIL import Image


def getTileSize(img):
    tileSize = 1
    indexY = img.size[1] // 2
    pixels = img.load()

    border_color = pixels[0, indexY]
    while pixels[tileSize, indexY] == border_color:
        tileSize += 1

    return tileSize


def convertToMaze(img, tileSize):
    pixels = img.load()

    border_pixel = pixels[0, 0]
    maze = []

    for y in range(0, img.size[1], tileSize):
        maze.append([])
        for x in range(0, img.size[0], tileSize):
            if pixels[x, y] == border_pixel:
                maze[len(maze) - 1].append("#")
            else:
                maze[len(maze) - 1].append(".")

    return maze


def generateMaze(path="maze.png"):
    img = Image.open(path)
    grayscale = img.convert('LA')

    tileSize = getTileSize(grayscale)
    mapa = convertToMaze(grayscale, tileSize)

    mapa[0][1] = "S"
    mapa[-1][-2] = "E"

    return mapa


if __name__ == '__main__':
    generateMaze()

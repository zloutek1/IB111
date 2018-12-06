import mazemaker


class Vector:
    def __init__(self, *args):
        self.parts = args

    def __add__(self, additor):
        addedParts = (parta + partb for parta, partb in zip(self, additor))
        return Vector(*addedParts)

    def __eq__(self, comparator):
        equalParts = (parta == partb for parta, partb in zip(self, comparator))
        return all(equalParts)

    @property
    def x(self):
        return self.parts[0]

    @property
    def y(self):
        return self.parts[1]

    @property
    def z(self):
        return self.parts[2]

    def __getitem__(self, index):
        return self.parts[index]

    def __repr__(self):
        return str(self.parts)


def findPath(maze, startPos=Vector(1, 0), endPos=Vector(-2, -1), position=None, steps=[]):
    if position is None:
        steps = [startPos]
        position = startPos + (0, 1)

    if position == endPos:
        return steps

    UPPOS = position + (0, -1)
    DOWNPOS = position + (0, 1)
    LEFTPOS = position + (-1, 0)
    RIGHTPOS = position + (1, 0)

    parsedSteps = []
    if maze[UPPOS.y][UPPOS.x] != "#" and UPPOS not in steps:
        retval = findPath(maze, startPos, endPos, UPPOS, steps + [position])
        if retval is not None and len(retval) > len(parsedSteps):
            parsedSteps = retval

    if maze[DOWNPOS.y][DOWNPOS.x] != "#" and DOWNPOS not in steps:
        retval = findPath(maze, startPos, endPos, DOWNPOS, steps + [position])
        if retval is not None and len(retval) > len(parsedSteps):
            parsedSteps = retval

    if maze[LEFTPOS.y][LEFTPOS.x] != "#" and LEFTPOS not in steps:
        retval = findPath(maze, startPos, endPos, LEFTPOS, steps + [position])
        if retval is not None and len(retval) > len(parsedSteps):
            parsedSteps = retval

    if maze[RIGHTPOS.y][RIGHTPOS.x] != "#" and RIGHTPOS not in steps:
        retval = findPath(maze, startPos, endPos, RIGHTPOS, steps + [position])
        if retval is not None and len(retval) > len(parsedSteps):
            parsedSteps = retval

    return parsedSteps


def displayPath(maze, steps):
    for step in steps:
        x, y = step
        maze[y][x] = "*"

    mazemaker.mprint(maze)


if __name__ == '__main__':
    ROWS = 101
    COLS = 101

    maze = mazemaker.generateMaze(ROWS, COLS)

    steps = findPath(maze, endPos=Vector(COLS - 2, ROWS - 1))
    displayPath(maze, steps)

"""
from PIL import Image
from math import sqrt


def mapValue(value, fromMin, fromMax, toMin, toMax):
    return (value - fromMin) * (toMax - toMin) / (fromMax - fromMin) + toMin


width = 600
height = 600
img = Image.new('RGB', (width, height), color=(73, 109, 137))

pixels = img.load()  # create the pixel map

iterationLimit = 200
treshold = 20

for y in range(img.size[1]):
    for x in range(img.size[0]):

        a = mapValue(x, 0, width, -2, 2)
        b = mapValue(y, 0, height, -2, 2)

        c = complex(a, b)
        z = 0

        count = 0
        while count < iterationLimit:
            z = z**2 + c

            if abs(z) > treshold:
                break

            count += 1

        bright = mapValue(count, 0, iterationLimit, 0, 1)
        bright = mapValue(sqrt(bright), 0, 1, 0, 255)
        bright = int(bright)

        if count == iterationLimit:
            bright = 0

        pixels[x, y] = (bright, bright, bright)

img.show()
"""


import tkinter
import turtle
from math import sin, cos, pi
from random import randint

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=800, height=800)
canvas.pack()

turtleScreen = turtle.TurtleScreen(canvas)
turtleScreen.delay(0)
turtleScreen.colormode(255)

t = turtle.RawTurtle(turtleScreen)
t.speed(0)


def circle(radius, *args, **kwargs):
    t.penup()
    t.right(90)
    t.forward(radius)
    t.left(90)

    t.pendown()
    t.circle(radius, *args, **kwargs)
    t.penup()

    t.penup()
    t.left(90)
    t.forward(radius)
    t.right(90)
    t.pendown()


def fractal(radius=300, steps=4, level=4, maxLevel=None):
    if not maxLevel:
        maxLevel = level

    if level == 1:
        turtleScreen.tracer(0)
        t.circle(radius)
        turtleScreen.tracer(1)
        return

    for angle in range(steps):
        if level < maxLevel - 2:
            turtleScreen.tracer(0)

        t.circle(radius, 360 // steps)

        if level < maxLevel - 2:
            turtleScreen.tracer(1)

        fractal(radius=radius // 2, level=level - 1, maxLevel=maxLevel)


def serpinski_circle(radius=300, level=5, maxLevel=None):
    if not maxLevel:
        maxLevel = level

    if level == 1:
        circle(radius)
        return

    if level < maxLevel - 3:
        turtleScreen.tracer(0)

    circle(radius)

    # right
    t.penup()
    t.forward(radius)
    t.pendown()
    serpinski_circle(radius / 2, level - 1)

    # left
    t.penup()
    t.backward(radius * 2)
    t.pendown()
    serpinski_circle(radius / 2, level - 1)

    # up
    t.penup()
    t.forward(radius)
    t.left(90)
    t.forward(radius)
    t.right(90)
    t.pendown()
    serpinski_circle(radius / 2, level - 1)

    t.penup()
    t.left(90)
    t.backward(radius)
    t.right(90)
    t.pendown()

    if level < maxLevel - 3:
        turtleScreen.tracer(1)


def kocho(length, level=6):
    if level == 1:
        t.fd(length)
    else:
        kocho(length * 1 / 3, level=level - 1)
        t.lt(60)
        kocho(length * 1 / 3, level=level - 1)
        t.rt(120)
        kocho(length * 1 / 3, level=level - 1)
        t.lt(60)
        kocho(length * 1 / 3, level=level - 1)


def kochoStar(length, level=6, angle=120):
    for i in range(360 // angle):
        kocho(length, level)
        t.rt(angle)


def rings(length, level):
    def recursion(length, level):
        if level == 0:
            t.forward(length)
            return

        distance = 10 / 2**(level * 1.75)
        recursion(distance, level=level - 1)
        recursion(distance, level=level - 1)

        for i in range(5):
            t.right(90)
            recursion(distance, level=level - 1)

        t.left(90)
        recursion(distance, level=level - 1)

    level += 1
    distance = 10 / 2**(level * 1.75)
    recursion(distance, level=level - 1)
    for i in range(3):
        t.right(90)
        recursion(distance, level=level - 1)


RADIUS = 200
mode = 4

if mode == 0:
    t.setpos(0, -300)
    t.clear()
    fractal(level=6)


if mode == 1:
    t.setpos(0, 0)
    t.clear()
    serpinski_circle(RADIUS, level=8)


if mode == 2:
    t.setpos(-300, 0)
    t.clear()
    kocho(RADIUS, level=6)


if mode == 3:
    t.setpos(0, 0)
    t.clear()
    kochoStar(RADIUS, level=6)


if mode == 4:
    t.setpos(100, 200)
    t.clear()
    rings(RADIUS, level=4)


root.mainloop()

#!/usr/bin/python3

import turtle

def draw_multicolor_square(t,sz):
    """Make turtle t draw a multi-color square of sz"""
    for i in ["red","purple","hotpink","blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(5)
size = 20
for i in range(15):
    draw_multicolor_square(tess,size)
    size=size+10
    tess.forward(10)
    tess.right(18)

wn.mainloop()
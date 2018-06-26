#!/usr/bin/python3
import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(2)
size = 1
for i in range(70):
    tess.forward(size)
    tess.right(90)
    size+=2
wn.mainloop()
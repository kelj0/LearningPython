#!/usr/bin/python3
import turtle

def draw_bar(t,height):
    """Get turtle t to draw one bar, of height."""
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write("  "+str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.forward(10)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue","red")
tess.pensize(4)

xs = [58,32,121,200,240,160,80]

for a in xs:
    draw_bar(tess,a)

wn.mainloop()
#! /usr/bin/python3
import turtle


def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order-1, size)
            t.left(angle)


def main():
    wn = turtle.Screen()
    alex = turtle.Turtle()
    wn.bgcolor("lightgreen")
    wn.title("Hello darkens my old friend")
    while True:
        koch(alex, 10, 10)


if __name__ == '__main__':
    main()
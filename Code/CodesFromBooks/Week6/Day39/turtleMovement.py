#!/usr/bin/python3
#!/usr/bin/python3
import turtle
import msvcrt

screen = turtle.Screen()

left = b'K'
right = b'M'
up = b'H'
down = b'P'
esc = b'\x1b'
player = turtle.Turtle()
player.shape("turtle")

speed = 10
while msvcrt.getch()!=esc:
    player.forward(speed)
    if msvcrt.getch()==left:
        player.left(10)
    elif msvcrt.getch()==right:
        player.right(10)
    
    if msvcrt.getch()==up:
        speed+=5
    elif msvcrt.getch()==down:
        speed-=5
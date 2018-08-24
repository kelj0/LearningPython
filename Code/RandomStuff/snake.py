#!/usr/bin/python3

import curses
import os
import time
import random

#-----CLASS-----#
class Snake():
    def __init__(self,startX,startY):
        self.x = startX
        self.y = startY
        self.s = 2
        self.t = [[startX-1,startY],[0,0]]
        self.direction = 'RIGHT'

    def size(self,siz=0):
        """Returns size of snake,
		optional parametar if you want to increase snake"""
        self.s += siz
        return self.s

    def tail(self,x,y):
        """Params: x,y
        Returns true if tail is in x,y"""
        for tail in self.t:
            if tail[0]==x and tail[1] == y:
                return True
        return False

    def setDirection(self, direction):
        self.direction = direction

#---------GLOBAL---------#
snake = Snake(20,10)
stdscr = curses.initscr()
key = curses.KEY_LEFT
foodX = random.randint(1,38)
foodY = random.randint(1,18)
#------------------------#

def drawBoard(snake):
    for y in range(0,20):
        for x in range(0,40):
            if y == 0 or y == 19 or x==0 or x==39:
                stdscr.addch(y,x,"*")
            elif snake.x == x and snake.y == y:
                stdscr.addch(y,x,"@")
            elif snake.tail(x,y):
                stdscr.addch(y,x,"o")
            elif foodX ==x and foodY == y:
                stdscr.addch(y,x,'$')
            else:
                stdscr.addch(y,x," ")
    stdscr.refresh()

# Check if you pressed buttons
def click():
    global key
    global snake
    
    key = stdscr.getch()

    if snake.direction!='UP' and snake.direction!='DOWN' and key == curses.KEY_UP:
        snake.setDirection('UP')
    elif snake.direction!='UP' and snake.direction!='DOWN' and key == curses.KEY_DOWN:
        snake.setDirection('DOWN')
    elif snake.direction!='RIGHT' and snake.direction!='LEFT' and key == curses.KEY_LEFT:
        snake.setDirection('LEFT')
    elif snake.direction!='RIGHT' and snake.direction!='LEFT' and key == curses.KEY_RIGHT:
        snake.setDirection('RIGHT')


# Move snake
def moveSnake():
    global snake

    snake.t[0][0] = snake.x
    snake.t[0][1] = snake.y

    if snake.size() > 1:
        for n in reversed(range(snake.size())):
            snake.t[n][0] = snake.t[n-1][0]
            snake.t[n][1] = snake.t[n-1][1]
        
    if snake.direction == "UP":
        snake.y-=1
    elif snake.direction == 'DOWN':
        snake.y+=1
    elif snake.direction == 'LEFT':
        snake.x-=1
    elif snake.direction == 'RIGHT':
        snake.x+=1


# Check if you died
def dead(snake):
    if snake.x==0 or snake.x==39 or snake.y == 0 or snake.y==19:
        return True
    if snake.size() > 1:
        if snake.tail(snake.x, snake.y):
            return True
    return False


def checkFood():
    global foodY,foodX,snake
    if snake.x == foodX and snake.y == foodY:
        snake.size(1)
        snake.t.append([0,0])
        SpawnNewFood()


def SpawnNewFood():
    global foodX,foodY
    foodX = random.randint(1,38)
    foodY = random.randint(1,18)


#----------------------------------------------------
def main():
    global snake
    global key
    curses.cbreak()
    stdscr.keypad(1)
    stdscr.nodelay(True)
    stdscr.addstr(20,0,"Press 'q' to quit")

    while not dead(snake):
        drawBoard(snake)
        checkFood()
        moveSnake()
        click()
        time.sleep(0.15)

        if key == ord('q'):
            break
    curses.endwin()


if __name__=='__main__':
    main()

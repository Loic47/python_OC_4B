import turtle
from time import *
from random import randint
t = turtle
t.shape("turtle")
turtle.colormode(255)
turtle.bgcolor("black")
t.color(randint(0,255),randint(0,255),randint(0,255))
t.speed(0)
t.pensize(1)
screenSize = 800
rayon = (screenSize-40)/6
nb_cercles = 200
turtle.tracer(100,0)

def dessinerTore ():
    t.ht()
    t.penup()
    t.forward(3*rayon)
    t.setheading(90)
    for i in range (nb_cercles):
        t.pendown()
        t.circle(rayon)
        t.penup()
        t.circle(3*rayon,360/nb_cercles)
        
        
while True:
    print(turtle.screensize())
    dessinerTore()
    sleep(2)
    t.reset()
    t.speed(0)
    t.color(randint(0,255),randint(0,255),randint(0,255))
    t.pensize(1)
    

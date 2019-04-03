import turtle
from time import sleep

#initialisation
screenSize = 480
turtle.setup(width=screenSize,height=screenSize,startx=800,starty=30)
turtle.colormode(255)
turtle.tracer(10)
t = turtle.Turtle(shape="turtle")
t.color("green")
t.penup()
t.speed(0)
t.pensize(1)
t.pencolor("green")

#fonction Hilbert à gauche
def hilbertG(step,long):
    if step != 0 :
        t.right(90)
        hilbertD(step-1,long)
        t.forward(long)
        t.left(90)
        hilbertG(step-1,long)
        t.forward(long)
        hilbertG(step-1,long)
        t.left(90)
        t.forward(long)
        hilbertD(step-1,long)
        t.right(90)

#fonction Hilbert à droite
def hilbertD(step,long):
    if step != 0 :
        t.left(90)
        hilbertG(step-1,long)
        t.forward(long)
        t.right(90)
        hilbertD(step-1,long)
        t.forward(long)
        hilbertD(step-1,long)
        t.right(90)
        t.forward(long)
        hilbertG(step-1,long)
        t.left(90)

#nouveau dessin
def nvDessin():
    n = turtle.numinput("Nombre de pas","Nombre de niveaux ?", default=5,minval=1)
    l = turtle.screensize()[0]/(2**n-1)
    t.reset()
    t.penup()
    t.color("green")
    t.speed(0)
    t.pensize(1)
    t.pencolor("green")
    t.goto(-turtle.screensize()[0]/2,-turtle.screensize()[0]/2)
    t.setheading(90)
    t.pendown()
    t.hideturtle()
    hilbertG(n,l)
    t.showturtle()
    t.penup()

       
#Programme principal
while True:
    nvDessin()
    sleep(2)

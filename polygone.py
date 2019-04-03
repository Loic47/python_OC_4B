import turtle
from time import*
from random import randint
t = turtle
t.shape("turtle")
turtle.colormode(255)
t.speed(0)
t.pensize(7)
t.hideturtle()
turtle.bgcolor(randint(100,180),randint(100,180),randint(100,180))
nb_cotes = int(turtle.numinput("Nombre de côtés", "Indiquez le nombre de côtés", 5))
if nb_cotes > 15 :
    t.tracer(0,0)

def dessiner_polygone (cotes, angle):
    for i in range (cotes):
        t.pendown()
        t.forward(750/nb_cotes)
        t.left(angle)
        
     
for n in range (36):
    angle = 360 / nb_cotes
    maCouleur =(randint(100,180),randint(100,180),randint(100,180))
    t.color(maCouleur)
    dessiner_polygone(nb_cotes,angle)
    t.left(10)
   
   
        
    
    

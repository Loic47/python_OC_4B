import turtle
import datetime



screensize = 800
turtle.setup(screensize,screensize,750,35)
turtle.colormode(255)
turtle.delay(0)
turtle.bgcolor(60, 200, 100)
c = turtle.Turtle()
h = turtle.Turtle()
m = turtle.Turtle()
s = turtle.Turtle("circle")
r_cadran = 200
petit = 5
grand = 10


#aiguilles
c.speed(0)
c.hideturtle()
s.speed(0)
s.shape("circle")
s.color(200, 100, 100)
s.turtlesize(1)
s_taille = r_cadran - grand
m.speed(0)
m.hideturtle()
m.color(200, 180, 180)
m.pensize(3)
m_taille = r_cadran - 3*grand
h.speed(0)
h.hideturtle()
h.color(150, 120, 150)
h.pensize(3)
h_taille = r_cadran - 6*grand
seconde = -1
minute = -1
heure = -1


#cadran
for i in range(60):
    if (i%15==0) :
        c.shape("triangle")
        c.setheading(i*90)
        c.penup()
        c.pensize(4)
        c.forward(215)
        #c.forward(185)
        c.pendown()
        #c.forward(30)
        c.stamp()
        c.penup()
        c.home()
    elif (i%5==0):
        c.shape("classic")
        c.setheading(i*30)
        c.penup()
        c.pensize(2)
        #c.forward(215)
        c.forward(185)
        c.pendown()
        c.forward(30)
        #c.stamp()
        c.penup()
        c.home()
    else:
        c.setheading(i*6)
        c.penup()
        c.pensize(1)
        c.forward(200)
        c.pendown()
        c.forward(15)
        c.penup()
        c.home()
        
        
#secondes
def dessinerSecondes(sec):
    s.clear()
    s.penup()
    s.hideturtle()
    s.goto(0,0)
    angle = (90-6*sec)
    s.setheading(angle)
    s.forward(s_taille)
    s.stamp()
    s.showturtle()
    turtle.update()
    

#minutes
def dessinerMinutes(mi):
    m.clear()
    m.penup()
    m.hideturtle
    m.goto(0,0)
    m.pendown()
    angle = 90-6*mi
    m.setheading(angle)
    m.forward(m_taille)
    turtle.update


#heures
def dessinerHeures(he):
    h.clear()
    h.penup()
    h.hideturtle
    h.goto(0,0)
    h.pendown()
    angle = 90-30*he
    h.setheading(angle)
    h.forward(h_taille)
    turtle.update
    
while True:
    sec = datetime.datetime.now().second
    if (sec != seconde):
        seconde = sec
        dessinerSecondes(sec)
    mi = datetime.datetime.now().minute
    if (mi != minute):
        minute = mi
        dessinerMinutes(mi)
    he = datetime.datetime.now().hour
    if (he != heure):
        heure = he
        dessinerHeures(he)


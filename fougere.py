import turtle


turtle.setup(width=480,height=360,startx=800,starty=30)
turtle.colormode(255)
t = turtle
t.shape("turtle")
turtle.bgcolor("black")
t.color("green")
t.penup()
t.goto(0,-300)
t.left(90)
t.speed(0)
t.setheading(90)
t.pensize(2)
t.pencolor("green")
longueur = 250
angle = 5

def dessinerFougère(longueur,angle):
    t.pendown()
    if longueur > 2:
        t.ht()
        turtle.tracer(100,0)
        t.forward(0.2*longueur)
        t.left(75)
        dessinerFougère(0.4*longueur,angle)
        t.right(150)
        dessinerFougère(0.4*longueur,angle)
        t.left(75)
        t.forward(0.2*longueur)
        t.right(angle)
        dessinerFougère(0.8*longueur,angle)
        t.left(angle)
        t.backward(0.4*longueur)
        
while True:
    dessinerFougère(longueur,angle)



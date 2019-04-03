import turtle

#initialisation
screenSize = 480
turtle.setup(width=screenSize,height=screenSize,startx=800,starty=30)
turtle.colormode(255)
turtle.delay(6)

t = turtle.Turtle(shape="turtle")
t.hideturtle()
t.penup()
t.shape("circle")
t.speed(0)
t.pensize(3)
t.pencolor("black")

#paramètres du bonhomme :
rayon_tete = 50
centre_tete = (0,150)
cou = (0,100)
epaules = (0,50)
bassin = (0,-50)
longueur_bras = 170
rayon_oeil = 6
rayon_bouche = .5*rayon_tete
epaisseur_oeil = 3
epaisseur_corps = 5
epaisseur_pantalon = 8
pied_droit = (-100,-200) #position du centre du pied
pied_gauche = (100, -200) #idem
pointure = 10
taille_soulier = 2



#dessiner la tête
def dessiner_tete():
    t.goto(0,100)
    t.pendown()
    t.circle(50)
    t.penup()
def dessiner_oeil():
    t.pensize(epaisseur_oeil)
    t.goto(-20,150)
    t.pendown()
    t.setheading(90)
    t.circle(rayon_oeil, 180)
    t.penup()
    t.goto(30,150)
    t.pendown()
    t.setheading(90)
    t.circle(rayon_oeil, 180)
    t.penup()
def dessiner_bouche():
    t.goto(-15,130)
    t.pendown()
    t.circle(15,180)
    t.penup()


#dessiner le corps
def dessiner_corps():
    t.pensize(epaisseur_corps)
    t.goto(cou)
    t.pendown()
    t.goto(bassin)
    


#dessiner les jambes
def dessiner_jambes():
    t.color("green")
    t.pensize(epaisseur_pantalon)
    t.goto(pied_droit)
    t.goto(bassin)
    t.goto(pied_gauche)


#dessiner un pied
def dessiner_pied():
    t.penup()
    t.goto(pied_droit)
    t.pensize(2)
    t.goto(-100,-200)
    t.color("red")
    t.stamp()
    t.goto(-90,-200)
    t.color("black")
    t.pendown()
    t.circle(10)
    t.penup()
    t.goto(pied_gauche)
    t.pensize(2)
    t.goto(100,-200)
    t.color("red")
    t.stamp()
    t.goto(110,-200)
    t.color("black")
    t.pendown()
    t.circle(10)


#dessiner les bras
def dessiner_bras(angle):
    t.color("black")
    t.pensize(3)
    t.setheading(90)
    t.penup()
    t.goto(epaules)
    t.pendown()
    t.left(angle)
    t.forward(longueur_bras)
    t.backward(longueur_bras)
    t.setheading(90)
    t.right(angle)
    t.forward(longueur_bras)
    t.backward(longueur_bras)
    t.setheading(90)


# Programme principal
while True:
    dessiner_tete()
    dessiner_oeil()
    dessiner_bouche()
    dessiner_corps()
    dessiner_jambes()
    dessiner_pied()
    dessiner_bras(-50)
    
    t.stop()
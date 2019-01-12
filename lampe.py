# Autor: J. Ostrzinski + Paul Teumer
# Datum: 21.12.2018
# Zweck: Klasse Lampe

from turtle import *
from time import*


# Die Klasse Lampe dient der Simulation einer zweidimensionalen Lampe
# im Turtle-Grafikfenster, dargestellt als schwarz ausgefüllter Kreis,
# wenn die Lampe aus ist, oder als farbig ausgefüllter Kreis, wenn sie an ist.
# Der Mittelpunkt der Lampe ist bei M(x,y), der Radius ist -radius-.
# Mit -farbe- wurd ihre Leuchtfarbe angegeben. Dabei muss der Farbstring für
# -farbe-, der beim Instanzieren einer Lampe übergeben werden muss, ein gültiger
# Farbstring des Moduls 'turtle' sein.
# Mit der Instanzierung erscheint die anfangs ausgeschaltete Lampe im Grafikfenster.
class Lampe:
    def __init__(self,x,y,radius,farbe):
        self.__x = x
        self.__y = y
        self.__radius = radius
        self.__farbe = farbe
        self.__bild = Turtle ()
        self.__bild.penup ()
        self.__bild.hideturtle ()
        self.__bild.goto(x,y)
        self.__bild.shape("circle")
        self.__bild.shapesize(radius/10)
        self.__bild.fillcolor("black")
        self.__bild.showturtle ()
        self.__leuchtet=False

    def anschalten (self):
        self.__leuchtet=True
        self.__bild.fillcolor(self.__farbe)

    def ausschalten(self):
        self.__leuchtet=False
        self.__bild.fillcolor("black")

    def verschieben (self,xneu,yneu):
        self.__x = xneu
        self.__y = yneu
        self.__bild.goto(xneu,yneu)

    def gibPos (self):
        return (self.__x,self.__y)
    def istAn (self):
        return self.__leuchtet
    def blinken(self,anzahl,anzeit,auszeit):
        for i in range(anzahl):
            self.__bild.fillcolor(self.__farbe)
            sleep(anzeit)
            self.__bild.fillcolor("black")
            sleep(auszeit)
    def gibLeuchtfarbe(self):
        return self.__farbe
    def setLeuchtfarbe(self,farbe):
        self.__farbe = farbe
        if self.__leuchtet == True:
            self.__bild.fillcolor(farbe)

#Paul Teumer
#08.01.2019
#Anzeige Fernsehbedinung

from turtle import *
from Fernseher import *
from time import *
from turtletools import *
from lampe import *
from _thread import *

def Dreieck ():
        pencolor("black")
        fillcolor("black")
        pendown()
        begin_fill()
        rt(90)
        fd(10)
        lt(120)
        fd(20)
        lt(120)
        fd(20)
        lt(120)
        fd(10)
        end_fill()
        penup()
        home()
class Gerät():
    def __init__(self):
        self.__hoehe = 400
        self.__breite = self.__hoehe / 2
        self.__screen = getscreen()
        self.__screen.setup (self.__breite+20,self.__hoehe+20)
        self.__programme = ["ARD","ZDF","RBB","SAT1","RTL","PRO7","KABEL1","ARTE","NDR"]
        hideturtle()
        tracer (False)
        penup()
        sprung(180,375)
        sprung(90,207)
        pendown()
        rechteck(770,395,"grey")
        penup()
        home()
        pendown()
        self.__Lan = Lampe(0,-50,20,"darkgreen")
        self.__Lan.anschalten()
        self.__LvolP = Lampe(50,100,20,"orange")
        self.__LvolP.anschalten()
        self.__LvolP2 = Lampe(50,50,20,"orange")
        self.__LvolP2.anschalten()
        self.__LPP = Lampe(-50,100,20,"yellow")
        self.__LPP.anschalten()
        self.__LMP = Lampe(-50,50,20,"yellow")
        self.__LMP.anschalten()
        penup()
        sprung(0,90)
        Dreieck()
        penup()
        sprung(0,60)
        lt(180)
        Dreieck()
        sprung(0,140)
        sprung(90,85)
        write("Programme",move=False,align='left',font=('Times New Roman',11,'normal'))
        sprung(270,105)
        write("Volumen",move=False,align='left',font=('Times New Roman',11,'normal'))
        tracer (True)
        self.__Fern = Fernseher()
        update()
        print("-----------------------------------------")
        print("Gelbe Tasten dienen zur Programmauswahl")
        print("Orangene Tasten dienen als Volumenauswahl")
        print("Die On/Off Taste ist Grün bzw. Rot")
        print("")
        print("Fernbedinung by Paul Teumer")
        print("-----------------------------------------")
        self.__screen.onclick(self.Klick,1)
    def Klick(self,x,y):
        self.__screen.onclick(None,1)
        x = x
        y = y
        self.__Klick(x,y)
    def __Klick(self,x,y):
        if -20<x<20 and -70<y<-30:
            Farbe = self.__Lan.gibLeuchtfarbe()
            if Farbe == "darkgreen":
                self.__Lan.setLeuchtfarbe("red")
            else:
                self.__Lan.setLeuchtfarbe("darkgreen")
            message = self.__Fern.anaus()
            if message == "ON":
                print("Fernseher angeschaltet.")
            elif message == "OFF":
                print("Fernseher ausgeschaltet.")
            else:
                print("Es ist ein Fehler aufgetreten")
        elif -70<x<-30 and 80<y<120:
            message = self.__Fern.ProgrammPlus()
            if message!="OFF":
                print("Neues Programm ist", self.__programme[message])
        elif -70<x<30 and 30<y<70:
            message = self.__Fern.ProgrammMinus()
            if message!="OFF":
                print("Neues Programm ist", self.__programme[message])
        elif 30<x<70 and 80<y<120:
            message = self.__Fern.VolPlus()
            if message!="OFF":
                print("Lautstärke", message,"%")
        elif 30<x<70 and 30<y<70:
            message = self.__Fern.VolMinus()
            if message!="OFF":
                print("Lautstärke", message,"%")
        self.__screen.onclick(self.Klick,1)

#|----------------#
#| Starting
#|   Main
#|   ...
#|
#|----------------#

Gerät = Gerät()
mainloop()

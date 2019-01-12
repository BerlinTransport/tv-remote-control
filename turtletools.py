# Autor: St. Schmidt
# Datum: 12.01.2017
# Zweck: Sammlung nützlicher Grafikroutinen 

from turtle import *

def sprung (winkel, weite):
# Vor.: Die Parameter -winkel- und -weite- sind Zahlen.
# Eff.: Die Position der Turtle ist wie folgt veraendert.
#       Die Turtle steht mit alter Ausrichtung/Blickrichtung an der Stelle, die sie erreicht,
#       wenn sie sich um  -winkel- in Grad gedreht hätte (positiver Drehsinn) und dann -weite-
#       vorwaerts gelaufen wäre. Sonst ist nichts verändert.
  penup()
  left(winkel)
  forward(weite)
  right(winkel)
  pendown()

def vollerKreis (radius, farbe):
# Vor.: Der Parameter -radius- ist ein positive Zahl, -farbe- ist ein String für eine
#       im turtle-Modul vordefinierte Farbe.
# Eff.: Um den aktuellen Standpunkt der Turtle ist ein mit -farbe- ausgefüllter Kreis
#       mit aktueller Stiftgröße gezeichnet. Der Rand hat auch die Farbe
#       -farbe-. Sonst ist nichts verändert.
  alteStiftfarbe = pencolor()
  alteFuellfarbe = fillcolor ()
  pencolor (farbe)
  fillcolor (farbe)
  forward (radius)
  left (90)
  begin_fill ()
  circle (radius)
  end_fill ()
  right (90)
  backward (radius)
  pencolor (alteStiftfarbe)
  fillcolor (alteFuellfarbe)

def rechteck (hoehe, breite, farbe):
# Vor.: Die Parameter hoehe und breite sind positive Zahlen,
#       farbe ist ein String für eine im turtle-Modul vordefinierte Farbe.
# Eff.: Ein mit 'farbe' ausgefuelltes Rechteck mit der Breite 'breite'
#       und der Hoehe 'hoehe' ist mit der aktuellen Stiftgröße gezeichnet.
#       Auch der Rand des Rechtecks ist mit der Farbe 'farbe' gezeichnet.
#       Dabei ist die linke untere Ecke die Position der Turtle, die 'Hoehenlinie'
#       in Turte-Richtung und die 'Breitenlinie' im 90-Grad-Winkel nach rechts von
#       der aktuellen Turtle-Richtung. Sonst ist nichts veraendert.
  altefuellfarbe=fillcolor() #Merke dir die alte Fuellfarbe
  altestiftfarbe=pencolor()  #Merke dir die alte Stiftfarbe
  fillcolor(farbe)
  pencolor(farbe)
  begin_fill()
  for i in range(2):
    forward(hoehe)
    right(90)
    forward(breite)
    right(90)
  end_fill()
  fillcolor(altefuellfarbe) # Aktiviere wieder die alte Fuellfarbe
  pencolor(altestiftfarbe) # Aktiviere wieder die alte Stiftfarbe

def stern(radius, farbe, ausrichtung):
# Vor.: Die Parameter -radius- und -ausrichtung- sind positive
#       Zahlen, -farbe- ist ein String für eine im turtle-Modul vordefinierte Farbe.
# Eff.: Ein regelmaessiger Stern mit fuenf Zacken ist in der Farbe -farbe-
#       mit der aktuellen Stiftgröße gezeichnet.
#       Auch der Rand des Sterns ist in der Farbe -farbe- gezeichnet.
#       Dabei ist der Mittelpunkt des Sterns die aktuelle Turtleposition, -ausrichtung-
#       gibt die Drehung des Sterns in Grad (positiver Drehsinn) an, bei ausrichtung=0
#       zeigt die oberste Zacke in Turtle-Richung. -radius- gibt den Radius des Kreises
#       (in Pixel) an, auf dem die Endpunkte der Zacken liegen, der Mittelpunkt des Kreises
#       ist die Turtleposition. Sonst ist nichts verändert.
  alteStiftfarbe = pencolor ()
  alteFuellfarbe = fillcolor ()
  left (ausrichtung)
  fillcolor (farbe)
  pencolor (farbe)
  sprung (0, radius)
  # Es folgt die trickreiche Ausfüllung!
  for i in range (5):
    begin_fill ()
    left (180)
    forward (radius)
    right (36)
    forward (radius)
    end_fill ()
  #Ausgangssituation wieder herstellen:
  sprung (180, radius)
  right (ausrichtung)
  pencolor (alteStiftfarbe)
  fillcolor (alteFuellfarbe)
  

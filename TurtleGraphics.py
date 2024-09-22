#TurtleGraphics.py
#Name: Samantha Roth
#Date: September 22, 2024
#Assignment: Lab4_Turtle Shapes

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(myTurtle, sides):
    for s in range(sides):
        myTurtle.forward(50)
        myTurtle.left(360/sides)
        
def fillCorner(myTurtle, corner):
    if corner == 2:
        drawSquare(myTurtle, 150)
        myTurtle.forward(75)
        myTurtle.begin_fill()
        drawSquare(myTurtle, 75)
        myTurtle.end_fill()
    
    elif corner == 3:
        drawSquare(myTurtle, 150)
        myTurtle.right(90)
        myTurtle.forward(75)
        myTurtle.left(90)
        myTurtle.begin_fill()
        drawSquare(myTurtle, 75)
        myTurtle.end_fill()
        
def main():
    myTurtle = turtle.Turtle()
    
    # drawSquare(myTurtle, 100)
    # drawPolygon(myTurtle, 5) 
    # drawPolygon(myTurtle, 8) 
    
    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()

"""
Drawing a circle with turtle module

Author: Brian Horner
Edit History:
9/5/2022 - Initial Version
"""

# imports
import math
import turtle

def drawCircleTurtle(x, y, r):
    """
    Drawing a circle using the turtle module
    :param x: x coordinate of center of circle
    :param y: y coordinate of center of circle
    :param r: radius of circle
    :return: drawing of circle
    """

    turtle.up()
    turtle.setpos(x+r, y)
    turtle.down()

    # iterate to draw the circle
    for i in range(0, 365, 5):
        a = math.radians(i)
        turtle.setpos(x+r*math.cos(a), y+r*math.sin(a))

if __name__ == '__main__':
    drawCircleTurtle(100, 100, 50)
    turtle.mainloop()

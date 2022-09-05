"""
Spirographs

Author: Brian Horner
Edit History:
9/5/2022 - Initial Version
"""

# imports
import math
import turtle

class Spiro(object):
    """

    """
    def __init__(self, xc, yc, col, R, r, l):

        # create turtle object
        self.t = turtle.Turtle()
        #set cursor shape
        self.t.shape('turtle')
        #set the step in degrees
        self.step = 5
        # set the drawing complete flag
        self.drawingComplete = False

        # set parameters
        self.setparams(xc, yc, col, R, r, l)

        # initialize the drawing
        self.restart()

    def setparams(self, xc, yc, col, R, r, l):
        """
        Setting the Spirograph parameters
        :param xc: x coordinate for center of curve
        :param yc: y coordinate for center of curve
        :param col: Color of Spirograph
        :param R: Large circle radius
        :param r: Small circle radius
        :param l:
        :return:
        """

        self.xc = xc
        self.yc = yc
        self.R = int(R)
        self.r = int(r)
        self.l = l
        self.col = col

        # reduce r/R to its smallest form by dividing with GCD
        gcdVal = math.gcd(self.r/self.R)
        self.nRot = self.r // gcdVal

        # get ratio of radii
        self.k = r/float(R)
        # set the color
        self.t.color(*col)
        # store the current angle
        self.a = 0

    def restart(self):
        """
        Restarts the drawing
        :return:
        """
        # set the flag
        self.drawingComplete = False
        # show the turtle
        self.t.showturtle()
        # go to the first point
        self.t.up()
        # Using local variables for cleaner code??
        R, k, l = self.R, self.k, self.l

        # Computing x and y coordinates with the angle set at 0 for curve
        # starting point
        a = 0.0
        x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = R*((1-k)*math.sin(a)-l*k*math.sin((1-k)*a/k))

        # Set position and set turtle down
        self.t.setpos(self.xc+x, self.yc+y)
        self.t.down()


    def draw(self):
        """
        Draw the Spirograph
        :return:
        """
        # using local variables for cleaner code??
        R, k, l = self.R, self.k, self.l

        # drawing the rest of the points of the Spirograph
        for i in range (0, 360*self.nRot+1, self.step):
            # calculating the new angle in radians
            a = math.radians(i)
            # calculating the x and y for the new angle
            x = R*((1-k)*math.cos(a)+l*k*math.cos((1-k)*a/k))
            y = R*((1-k)*math.sin(a)-l*k*math.sin((1-k)*a/k))
            # drawing line to that new position
            self.t.setpos(self.xc+x, self.yc+y)

        # hiding turtle after drawing
        self.t.hideturtle()

    def update(self):
        """
        # updating by one step??
        :return:
        """
        # skip rest of steps if done
        if self.drawingComplete:
            return
        # increment the angle
        self.a += self.step
        # draw a step
        
if __name__ == '__main__':


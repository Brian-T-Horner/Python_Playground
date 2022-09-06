"""
Spirographs

Author: Brian Horner
Edit History:
9/5/2022 - Initial Version
"""

# imports
import math
import turtle
import random


class SpiroAnimator:

    def __init__(self, N):
        """
        Constructor for class to animate Spirographs
        :param N: Numbers of spiros to be randomly generated
        """
        # set timer value in milliseconds
        self.deltaT = 10
        # get the window dimensions
        self.width = turtle.window_width()
        self.height = turtle.window_height()

        # create Spiro objects
        self.spiros = []
        for i in range(N):
            # generate random parameters
            rparams = self.genRandomParams()
            # set the spiro parameters
            spiro = Spiro(*rparams)
            self.spiros.append(spiro)
            # call timer
            turtle.ontimer(self.update, self.deltaT)

    def genRandomParams(self):
        """
        Generate random parameters for Spiros
        :return:
        """
        width, height = self.width, self.height

        # generate random integers for the radius of both circles
        R = random.randint(50, min(width, height)//2)
        r = random.randint(10, 9*R//10)

        # generate random float for the
        l = random.uniform(0.1, 0.9)

        # generate random x and y coordinate for start of Spiro
        xc = random.randint(-width//2, width//2)
        yc = random.randint(-height//2, height//2)
        col = (random.random(), random.random(), random.random())
        return (xc, yc, col, R, r, l)


class Spiro:

    def __init__(self, xc, yc, col, R, r, l):
        """
        Constructor for spiro class

        :param xc: x coordinate for the center of curve
        :param yc: y coordinate for the center of curve
        :param col: color of spirograph
        :param R: Radius of large circle
        :param r: radius of small circle
        :param l:
        """
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
        Restarts the drawing of spiros
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

        # using local variables for cleaner code??
        R, k, l = self.R, self.k, self.l

        # set the angle
        a = math.radians(self.a)

        # calculating x and y position
        x=self.R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y=self.R*((1-k)*math.sin(a)-l*k*math.sin((1-k)*a/k))
        # setting the new position & drawing line to that position at same time
        self.t.setpos(self.xc + x, self.yc +y)

        # if drawing is complete set the flag
        if self.a >= 360*self.nRot:
            self.drawingComplete = True
            # drawing is now done so hide turtle
            self.t.hideturtle()


if __name__ == '__main__':
    print("Hello")

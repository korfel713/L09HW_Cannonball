from math import sin, cos
from matplotlib import pyplot as plt

## Represent a cannonball, tracking its position and velocity.
#
class Cannonball:
    ## Create a new cannonball at the provided x position.
    #  @param x the x position of the ball
    #
    def __init__(self, x):
        self._x = x
        self._y = 0
        self._vx = 0
        self._vy = 0

    ## Move the cannon ball, using its current velocities.
    #  @param sec the amount of time that has elapsed.
    #
    def move(self, sec, grav=9.81):
        dx = self._vx * sec
        dy = self._vy * sec

        self._vy = self._vy - grav * sec

        self._x = self._x + dx
        self._y = self._y + dy

    ## Get the current x position of the ball.
    #  @return the x position of the ball
    #
    def getX(self):
        return self._x

    ## Get the current y position of the ball.
    #  @return the y position of the ball
    #
    def getY(self):
        return self._y

    ## Shoot the canon ball.
    #  @param angle the angle of the cannon
    #  @param velocity the initial velocity of the ball
    #
    def shoot(self, angle, velocity, user_grav):
        self._vx = velocity * cos(angle)
        self._vy = velocity * sin(angle)
        self.move(0.1, user_grav)

        while self.getY() > 1e-14:
            print("The ball is at (%.1f, %.1f)" % (self.getX(), self.getY()))

            plt.scatter(self.getX(), self.getY())
            plt.pause(.01)
            self.move(0.1, user_grav)

class Crazyball(Cannonball):

    def move(self):

        self.rand_q = random.randrange(0, 10)
        if self.getX():
            self._x = self._x + self.rand_q
        

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ##
    #  Demonstrate the cannonball class.
    #
    #from cannonball import Cannonball

    angle = float(input("Enter starting angle:"))
    v = float(input("Enter initial velocity:"))
    c = Cannonball(0)
    c.shoot(angle, v, 9.81)




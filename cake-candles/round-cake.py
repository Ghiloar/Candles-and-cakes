#see https://www.youtube.com/watch?v=l5gUrDg01cQ
#There was a possibility of having a candle on each sectoin of the cake of 0.3826008191706322 at iteration 1471000000.
from random import uniform as rand
from itertools import count

#initialization
k = 1 #length of radius
it = 10**7 #the number of iterations
oeis = 0 #One In Each Sector
output = 'There was a possibility of having a candle on each sectoin of the cake of {} at iteration {}.'

#every point is characterized by a pair of coordinates x and y
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
#the 2 candles
c1 = point(0, 0)
c2 = point(0, 0)
#the 2 points through which the line goes
r1 = point(0, 0)
r2 = point(0, 0)

#elaboration
#the candles must be within the circle
def validpoint(radius):
    xc = radius+1
    yc = radius+1
    while xc**2 + yc**2 > radius:
        xc = rand(-radius, radius)
        yc = rand(-radius, radius)
    p = point(xc, yc)
    return p

for i in count():
    #picks 4 random locations for the 4 points to be (within the circle)
    c1 = validpoint(k)
    c2 = validpoint(k)
    r1 = validpoint(k)
    r2 = validpoint(k)
    #calculates m and q from the coordinates of r1 and r2
    m = (r2.y-r1.y)/(r2.x-r1.x) #the angular coefficient of the line
    q = r1.y - m*r1.x #the point where the line intersects the y axis
    #there's one candle in each sector if and only if one candle is on one side of the line and the other candle is on the other side
    if (c1.y <= m*c1.x + q and c2.y > m*c2.x + q) or (c2.y <= m*c2.x + q and c1.y > m*c1.x + q):
        oeis += 1
    if i%(10**6) == 0 and i > 295*(10**6):
        oeisratio = oeis/i
        print(output.format(oeisratio, i))
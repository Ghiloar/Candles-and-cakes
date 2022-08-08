# see https://www[1]outube.com/watch?v=l5gUrDg01cQ
# There was a probability of having a candle
# on each section of the cake of
# 0.3826008191706322 at iteration 1471000000.
from random import uniform
from itertools import count

# Returns the coorrdinates of a point
# within a circle of equation x**2+y**2
def valid_point(radius):
    x = radius+1
    y = radius+1
    while x**2+y**2>radius:
        x = uniform(-radius, radius)
        y = uniform(-radius, radius)
    p = (x, y)
    return p


# Probability of having a candle
# on each section of the cake
probability = 0

radius = 1
output = 'There was a probability of having a candle on each \
          section of the cake of {} at iteration {}.'

# Cartesian coordinates of the 2 candles
candle_1 = (0, 0)
candle_2 = (0, 0)
# Cartesian coordinates of the 2 points
# through which the line goes
point_1 = (0, 0)
point_2 = (0, 0)


for i in count(1):
    candle_1 = valid_point(radius)
    candle_2 = valid_point(radius)
    point_1 = valid_point(radius)
    point_2 = valid_point(radius)
    
    # m is the angular coefficient of the line
    m = (point_2[1]-point_1[1])/(point_2[0]-point_1[0])
    # q is the point where the line intersects the y axis
    q = point_1[1] - m*point_1[0]
    
    # There's one candle in each sector if and only if
    # one candle is on one side of the line and the
    # other candle is on the other side.
    if (candle_1[1] <= m*candle_1[0] + q \
            and candle_2[1] > m*candle_2[0] + q) \
       or (candle_2[1] <= m*candle_2[0] + q \
           and candle_1[1] > m*candle_1[0] + q):
        probability += 1
    
    if i%(10**6) == 0 and i > 295*(10**6):
        print(output.format(probability/i, i))

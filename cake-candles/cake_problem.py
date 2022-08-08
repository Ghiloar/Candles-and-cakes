from random import random
from itertools import count
prob = 0
for i in count():
    c = random()
    cp = random()
    k = random()
    if c > cp:
        a = c
        c = cp
        cp = a
    if c < k and k < cp:
        prob += 1
    if i%10000000 == 0: 
        prob2 = prob/(i+1)
        print(prob2, i)
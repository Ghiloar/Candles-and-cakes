# For info see https://www.youtube.com/watch?v=FkVe8qrT0LA
from random import random
from itertools import count

# Probability of having a candle on each section of the cake
probability = 0

for i in count(1):
    candle_1 = random()
    candle_2 = random()
    knife = random()
    
    # The program assumes that candle_1 is smaller than
    # candle_2 so it swaps them if this is not the case
    if candle_1>candle_2:
        a = candle_1
        candle_1 = candle_2
        candle_2 = a
        
    if candle_1<knife and knife<candle_2:
        probability += 1
        
    if i%10**7==0: 
        print(probability/i, i)

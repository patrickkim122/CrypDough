import numpy as np
from numpy import genfromtxt
import talib

data = genfromtxt('BTCUSDT_2015-2023.csv', delimiter=',')
close = data[:,4]
# print(close)



rsi = talib.RSI(close)
print(rsi)

corrects = 0
incorrects = 0

for i, strength in enumerate(rsi):
    if strength > 80:
        price = close[i]
        print(f"At price {price} the RSI indicator had a value of {strength}, which implies that it was overbought")
        if close[i] > close[i+1]:
            corrects += 1
        else:
            incorrects += 1

    if strength < 20:
        price = close[i]
        print(f"At price {price} the RSI indicator had a value of {strength}, which implies that it was oversold")
        if close[i] < close[i+1]:
            corrects += 1
        else:
            incorrects += 1

print(f"the RSI indicator, over an 8 year span, was correct {corrects} times and incorrect {incorrects} times")
print(f"this was an overall accuracy of {corrects/(corrects + incorrects)}")

# 70 30 = 56%
# 75 25 = 56%
# 80 20 = 58%
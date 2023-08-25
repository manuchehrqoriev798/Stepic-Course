from math import *
n = int(input())
x = 0
for i in range(1, n):
    x = x + (1/(i+1))
    y = x + 1 - log(n)
print(y)
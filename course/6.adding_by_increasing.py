from math import *
n = int(input())
num1 = 0
for i in range(1, n):
    num1 = num1 + (1/(i+1))
print(num1 + 1 - log(n))
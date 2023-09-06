from math import factorial
num = int(input())
total = 0
for i in range(1, num + 1):
    i_factorial = factorial(i)
    total = total + i_factorial
print(total)
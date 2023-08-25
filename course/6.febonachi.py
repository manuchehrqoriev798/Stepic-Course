n = int(input())
first = 1
second = 0
for i in range(1, n+1):
    third = first
    first = third + second
    second = third
    print(third)

num = int(input())
counter = 1
for i in range(1, num+1):
    for j in range(1, 10):
        result = i + counter
        counter = counter + 1
        print(i, '+', j, '=', result )
    print()
    result = 0
    counter = 1
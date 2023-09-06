num = int(input())
counter = 1
for row in range(1, num + 1):
    for j in range(1, row + 1):
        print(counter, end=' ')
        counter = counter + 1
    print()
num = int(input())
for i in range(1, num + 1):
    total = ''
    for j in range(1, i + 1):
        if i % j == 0:
            total += '+'
    str_i = str(i)
    print(str_i + total)
        
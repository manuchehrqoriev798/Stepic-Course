total = 0
for x in range (1, 65):
    for y in range (1, 60):
        if x * 12 + y * 13 == 777:
            total += 1
            print('x =', x, 'y =', y)
print('Number of roots =', total)
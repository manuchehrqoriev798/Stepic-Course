total = 0
for n in range(1, 12):
    for k in range(1, 12):
        for m in range(1, 11):
            if 28 * n + 30 * k + 31 * m == 365:
                print('n =', n, 'k =', k, 'm =', m, end = '\n')
                total += 1
print('Number of roots is equal to', total)
m, p, n = float(input()), int(input()), int(input())
for day in range(1, n + 1):
    print(day, m)
    m = m * (1 + p/100)
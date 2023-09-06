for a in range(1, 151):
    for b in range(a, 151):
         for c in range(b, 151):
            for d in range(c, 151):
                x = a**5+b**5+c**5+d**5
                e = int(x**(1/5))
                if x == e**5:
                    print(a, b, c, d, e, a+b+c+d+e)
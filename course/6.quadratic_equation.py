from math import *
a, b, c = float(input()), float(input()), float(input())
diskriminant = b**2-4*a*c
if diskriminant < 0 :
    print('Нет корней')
elif diskriminant==0:
    print((-b)/(2*a))
else: 
    small_root = min( ((-b+sqrt(b**2-4*a*c))/(2*a)), ((-b-sqrt(b**2-4*a*c))/(2*a)) )
    big_root = max( ((-b+sqrt(b**2-4*a*c))/(2*a)), ((-b-sqrt(b**2-4*a*c))/(2*a)) )
    print(small_root, big_root, sep='\n')

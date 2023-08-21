a = int(input())
if a==0:
    print('зеленый')
if a>36 or a<0:
    print('ошибка ввода')
if 1<=a<=10 or 19>=a<=28:
    if a%2==0:
        print('черный')
    else:
        print('красный')
if 11<=a<=18 or 29>=a<=36:
    if a%2==1:
        print('черный')
    else:
        print('красный')

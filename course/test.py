a = int(input())
b = int(input())
c = input()
if c!='+' or c!='-' or c!='/' or c!='*':
    print('Неверная операция')
elif b==0 and c=='/':
    print('На ноль делить нельзя!')
elif c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='/':
    print(a/b)

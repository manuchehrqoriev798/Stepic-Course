m, n = int(input()), int(input())
if m%2==1 and m>0 :
    for i in range(m, n-1, -2):
        print(i)
elif m%2==0 and m>0:
    for i in range(m-1, n-1, -2):
        print(i)


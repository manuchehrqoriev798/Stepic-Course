yes = 0
no = 0
for i in range(10):
    num = int(input())
    if num%2==0:
        yes = yes + 1
    else: 
        no = no + 1
if yes==10:
    print('YES')
elif yes<10:
    print('NO') 
n = int(input())
flag = True
original_last_digit = n % 10
while n != 0:
    last_digit = n % 10
    if last_digit < original_last_digit:
        flag = False
    else: 
        original_last_digit = last_digit
    n = n // 10
if flag == True:
    print('YES')
else: 
    print('NO')
count = 0
mult_minus = 1
for i in range(10):
    num = int(input())
    if num >= 0:
        mult_minus = mult_minus * num
        count = count + 1
if count > 0:
    print(count)
    print(mult_minus)
else:
    print('NO')
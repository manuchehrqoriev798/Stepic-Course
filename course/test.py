num = int(input())
max_digit = -1
while num != 0:
    digit = num % 10
    if digit % 3 == 0:
        if digit > max_digit:
            max_digit = digit
    num = num // 10
if max_digit == -1:
    print('NO')
else:
    print(max_digit)
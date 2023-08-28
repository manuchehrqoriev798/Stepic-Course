n = int(input())
original_n = n
original_last_digit = n % 10
counter = 0
sum_number = 0

while n != 0:
    last_digit = n % 10
    counter = counter + 1
    sum_number = sum_number + last_digit
    n = n // 10

if sum_number / counter == original_last_digit and original_n // 10 ** (counter-1) == original_last_digit:
    print('YES')
else: 
    print('NO')
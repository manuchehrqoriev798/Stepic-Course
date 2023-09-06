num = int(input())
while num > 9:
    total = 0
    last_digit = num % 10
    total = total + last_digit
    num = num // 10
    num = total
print(num)
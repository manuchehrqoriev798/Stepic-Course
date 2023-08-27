n = int(input())
last_digit = 0
while n != 0:
    last_digit = n % 10
    print(last_digit)
    n = n // 10
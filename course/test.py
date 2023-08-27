n = int(input())
while n != 0:
    last_digit = n % 10
    last_digit = str(last_digit)
    last_digit = last_digit + ""
    n = n // 10
print(last_digit)
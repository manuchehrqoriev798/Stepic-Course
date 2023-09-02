n = int(input())
product = 1
while n > 0:
    last_digit = n % 10
    n //= 10
    product *= last_digit
print(product)
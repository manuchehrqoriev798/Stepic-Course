n = int(input())
original_n = n
counter = 0
while n != 0:
    last_digit = n % 10
    counter = counter + 1
    n = n // 10
the_second_digit = original_n // 10**(counter-2) - ((original_n // 10 ** (counter - 1)) * 10)
print(the_second_digit)
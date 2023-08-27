n = int(input())
minimum = 9
maximum = 0
while n > 0:
    x = n % 10
    if x < minimum:
        minimum = x
    if x > maximum:
        maximum = x
    n = n // 10
print('Максимальная цифра равна', maximum)
print('Минимальная цифра равна', minimum)


# n = int(input())
# max_digit = 0
# min_digit = 9

# while n > 0:
#     cur_digit = n % 10
    
#     max_digit = max(max_digit, cur_digit)
#     min_digit = min(min_digit, cur_digit)
    
#     n //= 10
    
# print("Максимальная цифра равна", max_digit)
# print("Минимальная цифра равна", min_digit)
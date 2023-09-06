start, end = int(input()), int(input())
max_sum = 0
number_with_max_sum = 0

for i in range(start, end + 1):
    current_sum = 0
    for j in range(1, i + 1):
        if i % j == 0:
            current_sum += j
    if current_sum >= max_sum:
        max_sum = current_sum
        number_with_max_sum = i

print(number_with_max_sum, max_sum)
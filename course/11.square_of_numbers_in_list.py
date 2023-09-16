numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
sum_numbers = 0
for i in range(len(numbers)):
    number = numbers[i]
    sum_numbers += number**2
print(sum_numbers)
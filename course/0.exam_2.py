# n = int(input())
# s = 0
# while n > 0:
#     last_digit = n % 10
#     if n % 2 == 0:
#         s += last_digit
#     n = n // 10
# print(s)

# n = int(input())
# s = 0
# while n > 0:
#     if n % 2 == 0:
#         s = s + n % 10
#     n = n // 10
# print(s)


# n = 8
# count = 0
# maximum = 0
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 4 == 0:
#         count += 1
#         if x > maximum:
#             maximum = x
#         elif x < maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')






# n = 4
# count = 0
# maximum = 0
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')




# num = int(input())
# print(19 * '*')
# for i in range(1, num - 1):
#     print('*', ' '*15, '*')
# print(19 * '*')
# n = int(input())
# for i in range(1, n + 1):
#     if i == 1 or i == n:
#         print('*' * 19)
#     else:
#         print('*' + ' ' * 17 + '*')


# num = int(input())
# while num > 99:
#     last_digit = num % 10
#     if num < 1000:
#         print(last_digit)
#         break
#     num = num // 10




# num = int(input())
# amount_3 = 0
# amount_last_digit = 0
# amount_juft = 0
# amount_0_and_5_combine = 0
# sum_number_bigger_than_5 = 0
# mult_number_bigger_than_7 = 1
# old_last_digit = num % 10
# while num != 0:
#     last_digit = num % 10
#     if last_digit == old_last_digit:
#         amount_last_digit += 1
#         old_last_digit = last_digit
#     if last_digit == 3:
#         amount_3 += 1
#     if last_digit == 0 or last_digit == 5:
#         amount_0_and_5_combine += 1
#     if last_digit % 2 == 0:
#         amount_juft += 1
#     if last_digit > 5:
#         sum_number_bigger_than_5 += last_digit
#     if last_digit > 7:
#         mult_number_bigger_than_7 *= last_digit
#     num = num // 10
# print(amount_3, amount_last_digit, amount_juft, sum_number_bigger_than_5, mult_number_bigger_than_7, amount_0_and_5_combine, sep = '\n')



# for i in range(1, 50):
#     for ii in range(1, 50):
#         for j in range(1, 50):
#             for jj in range(1, 50):
#                 if i**3 + ii**3 == j**3 + jj**3 and i != ii != j != jj and i**3 + ii**3 > 1729:
#                     print(i, ii, j, jj, i**3 + ii**3)




import datetime
start = datetime.datetime.now()

count = 0
for x1 in range(1, 33):
    if count == 5:
        break    
    for x2 in range(x1, 33):
        if count == 5:
            break
        for y1 in range(x1+1, x2):
            if count == 5:
                break
            for y2 in range(x2-1, y1, (-1)):
                if count == 5:
                    break
                if y1 ** 3 + y2 ** 3 == x1 ** 3 + x2 ** 3:
                    print(x1, x2, 'и', y1, y2, 's=', y1 ** 3 + y2 ** 3 )
                    count += 1  
                if count == 5:
                    break 
end = datetime.datetime.now()
print('Время выполнения кода =', end - start)

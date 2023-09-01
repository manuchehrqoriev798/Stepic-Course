max_minus_num = -10**6
sum_minus_num = 0
for i in range(10):
    num = int(input())
    if num < 0:
        sum_minus_num += num
    if num < 0 and num > max_minus_num:
        num = max_minus_num
print(sum_minus_num, max_minus_num, sep='\n')

# max_minus_num = 0
# sum_minus_num = 0
# for i in range(10):
#     num = int(input())
#     if num < 0:
#         sum_minus_num += num
#         if num < max_minus_num:
#             max_minus_num = num
# if sum_minus_num == 0:
#     print("NO")
# else:
#     print(sum_minus_num, max_minus_num, sep='\n')
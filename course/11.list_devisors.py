num = int(input())
new_list = []
for i in range(1, num+1):
    if num % i == 0:
        new_list.append(i)
print(new_list)
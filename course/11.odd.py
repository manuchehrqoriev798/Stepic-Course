num = int(input())
new_list = []
for i in range(1, num + 1):
    new_list.append(int(input()))
# print(new_list[0:len(new_list):2])
del new_list[1:len(new_list):2]
print(new_list)
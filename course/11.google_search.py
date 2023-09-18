num = int(input())
new_list = []
result_list = []
for i in range(1, num + 1):
    text = input()
    new_list.append(text)
find = input()
for i in range(0, len(new_list)):
    if find.lower() in new_list[i].lower():
        result_list.append(new_list[i])
print(*result_list, sep='\n')
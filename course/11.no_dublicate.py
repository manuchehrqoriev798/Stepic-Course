num = int(input())
new_list = []
old_text = ''
for i in range(1, num + 1):
    text = input()
    if text in new_list:
        continue
    else:
        new_list.append(text)
print(*new_list, sep='\n')
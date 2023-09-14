num = int(input())
old_element = 0
new_list = []
for i in range(1, num+1):
    element = int(input())
    new_list.append(element + old_element)
    old_element = element
del new_list[0]
print(new_list)
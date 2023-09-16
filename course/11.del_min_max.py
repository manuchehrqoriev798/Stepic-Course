numbers = int(input())
new_list = []
for i in range(0, numbers):
    num = int(input())
    new_list.append(num)
largest = max(new_list)
largest_index = new_list.index(largest)
del new_list[largest_index]
smallest = min(new_list) 
smallest_index = new_list.index(smallest)
del new_list[smallest_index]
print(*new_list, sep='\n')


num = int(input())
function = 0
new_list = []
for i in range(0, num):
    numbers = int(input())
    print(numbers, sep='\n')
    function = numbers**2 + 2*numbers + 1
    new_list.append(function)
print()
print(*new_list, sep = '\n')
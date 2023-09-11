# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# letters = ['a', 'b', 'c', 'd', 'e', 'f']
# print(len(numbers))
# print(len(letters))
# print(len([1, 2, 3]))
# print(len(list([1, 2, 3])))



# num = int(input())
# numbers = [0, num, 2]
# if 2 in numbers:
#     print('Список numbers содержит число 2')
# else:
#     print('Список numbers не содержит число 2')


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[:])
print(numbers[::-1])
print(numbers[0])
print(numbers[:4])
print(numbers[4:])

print(sum(numbers))
print(max(numbers))
print(min(numbers))
numbers[0] = 'Changed'
print(numbers)

print([1, 2, 3, 4] + ['a'])
print([1, 2]*3)
print([0]*10)
numbers = numbers + ['a', 'b', 'c']
print(numbers)

letters = ['a', 'b', 'c']
letters = letters + ['d'] + letters[2:] + letters[::-1]
print(letters)
# print(sum(numbers)) #this does not work because list of numbers now has also string
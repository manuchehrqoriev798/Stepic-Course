# num = int(input())
# list_numbers = list(range(1, num+1, 1))
# print(list_numbers)


# print(str(list(range(1, int(input()) + 1))))

# num = int(input())
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print(alphabet[:num])

num = int(input())
s = ''
for i in range(0, num+1):
    s = s + chr(97 + i)
print(list(s))
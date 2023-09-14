# text = input()
# for i in range(0, len(text)):
#     if i % 3 != 0:
#         print('' + text[i], end='')

# s = input()
# for i in range(0, len(s)):
#     if i % 3 == 0:
#         continue
#     else:
#         print(s[i], end='')

# text = input()
# new_text = ''
# for i in range(0, len(text)):
#     if text[i] == '1':
#         new_text = text.replace('1', 'one')
# if len(new_text) > 1:
#     print(new_text)
# else: 
#     print(text)

# text = input()
# res = text.replace('@', '')
# print(res)


# text = input()
# counter = 0
# for i in range(0, len(text)):
#     if text[i]=='f':
#         counter += 1
#     if counter == 2:
#         print(i)
#         break
# if counter == 1:
#     print('-1')
# elif counter == 0:
#     print('-2')


text = input()
first = text.find('h')
last = text.rfind('h')
reverse = text[first+1:last]
reverse_final = reverse[::-1]
print(text[0:first+1] + reverse_final + text[last:])
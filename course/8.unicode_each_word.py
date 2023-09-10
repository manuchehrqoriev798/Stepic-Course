# text = input()
# start = ''
# space = ' '
# for i in range(0, len(text)):
#     code = ord(text[i])
#     code_str = str(code)
#     start = start + code_str + space
# print(start)


text = input()
for i in range(0, len(text)):
    code = str(ord(text[i]))
    print(code, end=' ')

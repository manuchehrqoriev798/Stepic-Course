# text = input()
# counter = 0
# for i in range(0, len(text)):
#     if text[i] in '1234567890':
#         counter += 1
# print(counter)

text = input()
counter = 0
for i in range(10):
    counter += text.count(str(i))
print(counter)
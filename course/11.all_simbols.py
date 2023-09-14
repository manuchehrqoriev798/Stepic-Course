num = int(input())
empty_text = ''
main_list = []
for i in range(num):
    text = input()
    empty_text += text
main_list.extend(empty_text)
print(main_list)


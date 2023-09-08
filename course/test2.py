num = int(input())
start = ''
reminder_num = 0
reminder_str = 0
num_str = str(num)
for i in range(0, num + 1):
    reminder_num = num_str[i] // 2
    reminder_str = str(reminder_num)
    start = start + reminder_str
print(start)

#     if text[i] in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
#         counter_a += 1
#     if text[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
#         counter_b += 1
# print('Количество гласных букв равно', counter_a)
# print('Количество согласных букв равно', counter_b)
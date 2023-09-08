text = input()
counter_a = 0
counter_b = 0
for i in range(0, len(text)):
    if text[i] in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
        counter_a += 1
    if text[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        counter_b += 1
print('Количество гласных букв равно', counter_a)
print('Количество согласных букв равно', counter_b)
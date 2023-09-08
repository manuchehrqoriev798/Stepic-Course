test = input()
counter_plus = 0
counter_mult = 0
for i in range(0, len(test)):
    if test[i] in '+':
        counter_plus += 1
    if test[i] in '*':
        counter_mult += 1
print('Символ + встречается', counter_plus, 'раз')
print('Символ * встречается', counter_mult, 'раз')
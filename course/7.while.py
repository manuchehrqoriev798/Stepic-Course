counter = 0
n = input()
while n != 'достаточно' and n != 'хватит' and n != 'стоп' :
    counter = counter + 1
    n = input()
print(counter)
name = input()
counter = 0
for i in range(1, len(name)):
    if  name[i]  in 'abcdefghijklmnopqrstuvwxyz':
        counter += 1
print(counter)


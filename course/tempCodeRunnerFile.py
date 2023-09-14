text = input()
counter = 0
for i in range(0, len(text)):
    if text[i]=='f':
        counter += 1
    if counter == 2:
        print(i)
if counter==1:
    print('-1')
elif counter == 0:
    print('-2')
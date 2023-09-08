text = input()
counter = 0
start = ''
for i in range(0, len(text)):
    if start == text[i]:
        counter += 1
    start = text[i]
print(counter)
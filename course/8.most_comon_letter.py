text = input()
counter_1 = 0
counter_2 = 0
for i in range(0, len(text)):
    counting = text.count(text[i])
    if counting >= counter_1:
        counter_1 = counting
        counter_2 = i
print(text[counter_2])
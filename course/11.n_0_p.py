negative = []
positive = []
zero = []
for i in range(0, int(input())):
    num = int(input())
    if num < 0:
        negative.append(num)
    if num == 0:
        zero.append(num)
    if num > 0:
        positive.append(num)
print(*(negative + zero + positive), sep = '\n')
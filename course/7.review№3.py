total = 0
for i in range(7):
    num = int(input())
    if num % 2 == 0:
        total += num
if total > 0:
    print(total)
else:
    print(0)

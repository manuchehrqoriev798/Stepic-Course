num = int(input())
all_reminder_str = ''
result = ''
while num != 0:
    full = num // 2
    reminder = num % 2
    num = full
    reminder_str = str(reminder)
    all_reminder_str += reminder_str
for i in range(len(all_reminder_str)-1, -1, -1):
    result += all_reminder_str[i]
print(result)

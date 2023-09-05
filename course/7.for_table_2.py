num = int(input())
n = 0
for i in range(num):
    for j in range(5):
        print(i + 1, end=' ')  # Print 'i+1' instead of 'num'
    print()  # Move this print statement outside the inner loop
num = int(input())
total = 0
factorial_i = 1  # Initialize the factorial for the first number (1! = 1)

for i in range(1, num + 1):
    factorial_i *= i  # Update the factorial for the current number by multiplying with i
    total += factorial_i  # Add the factorial to the total

print(total)
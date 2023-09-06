num = int(input())
counter = 1
for i in range(1, num + 1):
    i_str = str(i)  # Convert i to a string
    print(i_str * counter)
    counter = counter + 1
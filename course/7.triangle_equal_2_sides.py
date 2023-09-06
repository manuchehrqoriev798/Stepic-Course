num = int(input())
max_point = num // 2 + 1
star = '*'
star_before_max = 0
star_after_max = 0
counter = 0
for i in range(1, num + 1):
    if i <= max_point:
        star_before_max = i * star
        counter = counter + 1
        print(star_before_max)
    else:
        star_after_max = (counter - 1) * star
        print(star_after_max)
        counter = counter - 1


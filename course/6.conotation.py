city1, city2, city3 = input(), input(), input()
length_city1 = len(city1)
length_city2 = len(city2)
length_city3 = len(city3)
print(length_city1)
longest = max(length_city1, length_city2, length_city3)
shortest = min(length_city1, length_city2, length_city3)
if longest==length_city1 and shortest==length_city2:
    print(city2, city1, sep='\n')
elif longest==length_city2 and shortest==length_city1:
    print(city1, city2, sep='\n')
elif longest==length_city2 and shortest==length_city3:
    print(city3, city2, sep='\n')
elif longest==length_city3 and shortest==length_city2:
    print(city2, city3, sep='\n')
elif longest==length_city1 and shortest==length_city3:
    print(city3, city1, sep='\n')
else: 
    print(city1, city3, sep='\n')


mult = 1
for i in range(1, 11):
   if i % 2 == 0:
      continue
   if i % 9 == 0:
      break
   mult *= i
print(mult)
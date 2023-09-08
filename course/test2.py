# word = input()
# half_word = len(word) // 2
# if len(word) % 2 ==0 and half_word >= 2:
#     print(word[-half_word:] + word[:half_word])
# if len(word) % 2 != 0 and half_word >= 2:
#     print(word[-half_word:] + word[:half_word+1] )
# if len(word) == 1:
#     print(word[0])
# if len(word) == 2:
#     print(word[1] + word[0])

from math import *
s = input()
i = ceil(len(s)/2)
print(s[i:]+s[:i])

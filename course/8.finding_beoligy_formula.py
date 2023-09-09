text = input()
text = text.lower()
print('Аденин:', text.count('а'))
print('Гуанин:', text.count('г'))
print('Цитозин:', text.count('ц'))
print('Тимин:', text.count('т'))


# text = input()
# adenin = 0
# guanin = 0
# tsitozin = 0
# timin = 0
# for i in range(0, len(text)):
#     if text[i] in 'Аа':
#         adenin += 1
#     if text[i] in 'Гг':
#         guanin += 1
#     if text[i] in 'Цц':
#         tsitozin += 1
#     if text[i] in 'Тт':
#         timin += 1
# print('Аденин:', adenin)
# print('Гуанин:', guanin)
# print('Цитозин:', tsitozin)
# print('Тимин:', timin)
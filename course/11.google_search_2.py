# num = int(input())
# new_list = []
# result_list = []
# start = ''
# for i in range(1, num + 1):
#     text = input()
#     new_list.append(text)
# amount_of_search = int(input())
# for i in range(1, amount_of_search + 1):
#     text_to_find = input()
#     text_to_find += start
# for i in range(0, len(new_list)):
#     if text_to_find.lower() in new_list[i].lower():
#         result_list.append(new_list[i])
# print(*result_list, sep='\n')





num = int(input())
main_list = []
search_list = []
result_list = []

# Collect items for main_list
for i in range(num):
    text = input()
    main_list.append(text)

# Collect items for search_list
for ii in range(int(input())):
    search_list.append(input().lower())  # Convert to lowercase here

for iii in range(len(main_list)):
    if all(search_item in main_list[iii].lower() for search_item in search_list):
        result_list.append(main_list[iii])

print(*result_list, sep='\n')



num = int(input())
main_list = []
for i in range(num):
    text = input()  
    main_list.append(text)
k = int(input()) -1
for j in range(num):
    if len(main_list[j]) > k:
        print(main_list[j][k], end='')
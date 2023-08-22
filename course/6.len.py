str1, str2, str3 = input(), input(), input()
length_str1=len(str1)
length_str2=len(str2)
length_str3=len(str3)
if  (2*length_str2-length_str3-length_str1)*(2*length_str3-length_str1-length_str2)*(2*length_str1-length_str2-length_str3)==0:
    print('YES')
else: 
    print('NO')
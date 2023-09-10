k = int(input())
text = input()
for i in range(0, len(text)):
    code = ord(text[i])
    code = code - k
    if code < 97:
        while code < 97:
            code = code + 26
    if code > 123:
        while code > 123:
            code = code - 26
    print(chr(code), end='')
    # wfmrfygwfy
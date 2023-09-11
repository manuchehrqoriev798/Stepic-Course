text = input()
first = text.find('h')
last = text.rfind('h')
result = text[:first] + text[last+1:]
print(result)




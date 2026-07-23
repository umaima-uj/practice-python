import re
text = "alice has 3 apples,Bob has 15 oranges,and charlie has 250 bananas:"
numbers = re.search(r'\d+',text)
words= re.findall(r'\w',text)
digit = re.split(r'\d+',text)
change= re.sub(r'\d+',"X",text)
print(numbers)
print(words)
print(digit)
print(change)
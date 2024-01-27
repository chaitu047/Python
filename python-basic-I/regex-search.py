import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)

print(search.span()[0])

if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")
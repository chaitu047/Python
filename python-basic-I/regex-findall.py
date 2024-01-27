import re

text = "The quick brown brown brown fox"
pattern = r"brown"

search = re.findall(pattern, text)

print(search)

if search:
    print("Pattern found:", search)
else:
    print("Pattern not found")
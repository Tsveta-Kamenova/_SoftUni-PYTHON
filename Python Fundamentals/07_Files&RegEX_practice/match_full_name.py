import re

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
names = input()

matches = re.findall(pattern, names)

for match in matches:
    print(match, end=" ")
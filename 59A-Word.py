word = str(input())
up, low = 0, 0

for c in word:
    if c.isupper():
        up += 1
    else:
        low += 1

print(word.upper() if up > low else word.lower())
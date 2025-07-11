games = int(input())
word = str(input())

a, d = 0, 0

for c in word:
    if c == 'A':
        a += 1
    else:
        d += 1

if a == d:
    print("Friendship")
elif a > d:
    print("Anton")
else:
    print("Danik")
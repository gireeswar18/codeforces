t = int(input())

for _ in range(t):
    word = str(input())
    a, b = 0, 0

    for c in word:
        if c == 'A':
            a += 1
        else:
            b += 1

    print("A" if a > b else "B")
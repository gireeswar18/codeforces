t = int (input())

for _ in range(t):
    arr = str(input())

    a, b, c = 0, 0, 0

    for x in arr:
        if x == 'A':
            a += 1
        elif x == 'B':
            b += 1
        else:
            c += 1

    take = min(a, b)
    a -= take
    b -= take

    take = min(b, c)
    a -= take
    b -= take

    print("YES" if (a + b + c == 0) else "NO")
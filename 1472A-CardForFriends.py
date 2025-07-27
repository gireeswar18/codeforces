t = int(input())

for _ in range(t):
    w, h, n = map(int, input().split())
    if n == 1:
        print("YES")
        continue

    res = 1

    while w % 2 == 0 and res < n:
        res *= 2
        w = w // 2

    while h % 2 == 0 and res < n:
        res *= 2
        h = h // 2

    print("YES" if res >= n else "NO")
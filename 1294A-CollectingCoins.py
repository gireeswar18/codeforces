t = int(input())

for _ in range(t):
    a, b, c, n = map(int, input().split())

    max_coins = max(a, b, c)

    n -= (max_coins - a)
    n -= (max_coins - b)
    n -= (max_coins - c)

    if n >= 0 and n % 3 == 0:
        print("YES")
    else:
        print("NO")
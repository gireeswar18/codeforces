t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_min = min(a)
    b_min = min(b)

    res = 0

    for i in range(n):
        res += max(a[i] - a_min, b[i] - b_min)

    print(res)
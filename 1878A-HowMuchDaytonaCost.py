t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    res = "NO"
    for num in arr:
        if num == k:
            res = "YES"
            break

    print(res)
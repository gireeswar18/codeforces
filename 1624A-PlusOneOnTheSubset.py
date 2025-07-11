t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    mx = max(arr)
    mn = min(arr)

    print(mx - mn)
t = int(input())

for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))
    arr = sorted(arr)
    res = "YES"

    for i in range(1, n):
        if arr[i] <= arr[i - 1]:
            res = "NO"
            break

    print(res)
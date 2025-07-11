t = int(input())

for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    if n < 3:
        print(-1)
        continue

    arr = sorted(arr)
    res = -1

    for i in range(n - 2):
        if arr[i] == arr[i + 2]:
            res = arr[i]
            break
    
    print(res)
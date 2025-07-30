t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = float("inf")


    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            res = 0
            break
        else:
            res = min(((arr[i] - arr[i - 1]) // 2) + 1, res)
        
    print(res)
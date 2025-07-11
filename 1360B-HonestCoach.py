t = int(input())

for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    arr = sorted(arr)
    min_diff = 1001
    
    for i in range(1, n):
        min_diff = min(min_diff, arr[i] - arr[i - 1])

    print(min_diff)
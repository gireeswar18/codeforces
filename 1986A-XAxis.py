t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))
    arr = sorted(arr)

    a = arr[1]

    res = 0
    for num in arr:
        res += abs(num - a)

    print(res)
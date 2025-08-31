t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    ptr = 0

    for i in range(n):
        if arr[i] >= 0:
            arr[ptr], arr[i] = arr[i], arr[ptr]
            ptr += 1

    res = 0
    for num in arr:
        if num < 0:
            res += -num
        else:
            res += num

    print(res)    
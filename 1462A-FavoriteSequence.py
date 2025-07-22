t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    l = 0
    r = n - 1
    while l < r:
        print(arr[l], end = " ")
        print(arr[r], end = " ")

        l += 1
        r -= 1
    
    if n % 2 == 1:
        print(arr[n // 2])
    else:
        print()

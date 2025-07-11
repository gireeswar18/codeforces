import math
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    total = sum(arr)

    res = math.sqrt(total)
    if float(math.floor(res)) == res:
        print("YES")
    else:
        print("NO")
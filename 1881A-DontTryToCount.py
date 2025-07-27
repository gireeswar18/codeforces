t = int(input())

for _ in range(t):
    m, n = map(int, input().split())
    x = str(input())
    s = str(input())

    arr = list(x)
    op = 0
    res = -1

    if s in x:
        print(0)
        continue

    while len(arr) <= 50:
        arr.extend(arr[:])
        op += 1

        if s in "".join(arr):
            res = op
            break


    print(res)
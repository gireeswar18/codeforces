t = int(input())

for _ in range(t):
    a = str(input())
    n = len(a)

    res = ['x' for _ in range(n)]

    for i in range(n):
        if a[i] == 'p':
            res[n - i - 1] = 'q'
        elif a[i] == 'q':
            res[n - i - 1] = 'p'
        else:
            res[n - i - 1] = 'w'

    print("".join(res))
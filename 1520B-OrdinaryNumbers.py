t = int(input())

for _ in range(t):
    n = int(input())
    res = 0
    div = 1
    bound = 9

    while n > bound:
        res = res + 9
        bound = bound * 10 + 9
        div = div * 10 + 1

    res += (n // div)

    print(res)
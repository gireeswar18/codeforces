t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a = sorted(a)
    b = sorted(b)

    # check if we can swap if not then stop
    i = 0
    j = n - 1

    while (i < n and j >= 0 and k != 0):
        if a[i] < b[j]:
            a[i], b[j] = b[j], a[i]
            i += 1
            j -= 1
            k -= 1
        else:
            j -= 1

    print(sum(a))
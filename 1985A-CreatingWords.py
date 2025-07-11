t = int(input())

for i in range(t):
    a, b = map(str, input().split())

    list_a = list(a)
    list_b = list(b)

    list_a[0], list_b[0] = list_b[0], list_a[0]

    print("".join(list_a), "".join(list_b))
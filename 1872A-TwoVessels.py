t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    diff = abs(a - b)
    ops = 0

    while diff != 0:
        if diff > c * 2:
            diff -= (c * 2)
        else:
            diff = 0
        ops += 1

    print(ops)

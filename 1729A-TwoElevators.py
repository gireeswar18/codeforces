t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    taking_elev1 = abs(a - 1)
    taking_elev2 = abs(b - c) + abs(c - 1)

    if taking_elev1 == taking_elev2:
        print(3)
    elif taking_elev1 < taking_elev2:
        print(1)
    else:
        print(2)
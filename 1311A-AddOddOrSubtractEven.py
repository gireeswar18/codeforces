t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    if a == b:
        print(0)
    elif a < b:
        # 15 25 = (10) 2
        # 8 12 = (4) 2
        # 7 12 = (5) 1
        # 8 15 = (7) 1

        if (b - a) % 2 == 0:
            print(2)
        else:
            print(1)
    else:
        # 25 15 = (10) 1
        # 12 8 = (4) 1
        # 12 7 = (5) 2
        # 15 8 = (7) (2)

        if (a - b) % 2 == 0:
            print(1)
        else:
            print(2)

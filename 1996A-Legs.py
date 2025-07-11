t = int(input())

for _ in range(t):
    n = int(input())

    cnt = n // 4

    if n % 4 == 0:
        cnt = n // 4
    else:
        cnt = (n // 4) + 1

    print(cnt)
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    arr = list(map(int, input().split()))

    gold = 0
    res = 0

    for c in arr:
        if c >= k:
            gold += c
        elif c == 0 and gold != 0:
            gold -= 1
            res += 1

    print(res)
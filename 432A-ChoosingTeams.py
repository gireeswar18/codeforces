n, k = map(int, input().split())

lt = list(map(int, input().split()))

eligible = 0

for x in lt:
    if 5 - x >= k:
        eligible += 1


print(eligible // 3)
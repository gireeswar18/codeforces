n = int(input())
cnt = 0

for tl in range(1, (n // 2) + 1):
    if (n - tl) % tl == 0:
        cnt += 1

print(cnt)
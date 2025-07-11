n = int(input())
stones = str(input())

cnt = 0

for i in range(1, n):
    if stones[i] == stones[i - 1]:
        cnt += 1

print(cnt)
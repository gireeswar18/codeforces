cal = list(map(int, input().split()))
seq = str(input())
res = 0

for s in seq:
    sq = int(s)
    res += cal[sq - 1]

print(res)
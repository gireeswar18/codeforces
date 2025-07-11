n = int(input())

arr = list(map(int, input().split()))

res = 0

maxBurles = max(arr)

for b in arr:
    res += (maxBurles - b)

print(res)    
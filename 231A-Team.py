sums = int(input())
res = 0
for i in range(sums):
    a, b, c = map(int, input().split())
    if a + b + c > 1:
        res += 1

print(res)
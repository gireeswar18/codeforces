k, n, w = map(int, input().split())

needed = 0
for i in range(1, w + 1):
    needed += (i * k)

print(needed - n if n < needed else 0)
n, k = map(int, input().split())

heights = list(map(int, input().split()))
width = 0

for h in heights:
    if h > k:
        width += 1
    width += 1

print(width)
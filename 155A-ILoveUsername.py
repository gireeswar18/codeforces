t = int(input())

lt = list(map(int, input().split()))

cnt = 0
max_pts = lt[0]
min_pts = lt[0]

for pts in lt:
    if pts > max_pts:
        cnt += 1
        max_pts = pts
    if pts < min_pts:
        cnt += 1
        min_pts = pts
    
print(cnt)
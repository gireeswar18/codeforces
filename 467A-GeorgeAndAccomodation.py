n = int(input())
cnt = 0

for i in range(n):
    occupied, capacity = map(int, input().split())

    if capacity - occupied >= 2:
        cnt += 1
    
print(cnt)
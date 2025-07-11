t = int(input())

for i in range(t):
    lt = list(map(int, input().split()))

    cnt = 0

    for d in lt:
        if d > lt[0]:
            cnt += 1
    
    print(cnt)
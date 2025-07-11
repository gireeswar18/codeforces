t = int(input())

for _ in range(t):
    n = int(input())

    cnt = 0

    for i in range(1, (n//2) + 1):
        if n - i != i:
            cnt += 2
        else:
            cnt += 1
    
    print(cnt)
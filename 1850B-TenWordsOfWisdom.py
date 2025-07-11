t = int(input())

for _ in range(t):
    n = int(input())
    res = 0
    resp = 1

    for i in range(n):
        a, b = map(int, input().split())

        if a <= 10 and b > res:
            res = b
            resp = i + 1
        
    print(resp)
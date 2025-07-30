t = int(input())

for _ in range(t):
    a, b, n = map(int, input().split())

    if a < b:
        a, b = b, a
    
    op = 0

    while a <= n:
        temp = a
        a = a + b
        b = temp
        op += 1

    print(op)
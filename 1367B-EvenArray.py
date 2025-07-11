t = int(input())

for i in range(t):
    n = int(input())

    lt = list(map(int, input().split()))
    even = 0
    odd = 0

    for i in range(n):
        if i % 2 != lt[i] % 2:
            if lt[i] % 2 == 0:
                even += 1
            else:
                odd += 1
    
    if even != odd:
        print(-1)
    else:
        print((even + odd) // 2)
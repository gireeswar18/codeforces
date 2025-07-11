t = int(input())

for i in range(t):
    a, b = map(int, input().split())

    if a > b:
        a, b = b, a

    diff = b - a
    cnt = 0
    k = 10

    while diff != 0:
        if diff >= k:
            cnt += (diff // k)
            diff %= k
        else:
            k -= 1
    
    print(cnt)
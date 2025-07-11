t = int(input())

for _ in range(t):
    n, x = map(int, input().split())

    if n <= 2:
        print(1)
        continue

    end = 3 + x - 1
    res = 2

    while n > end:
        end = end + x
        res += 1
    
    print(res)
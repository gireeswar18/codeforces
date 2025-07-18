t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())

    left = list(map(int, input().split()))
    right = list(map(int, input().split()))

    res = 0

    for l in left:
        if l < k:
            for r in right:
                if l + r <= k:
                    res += 1
    
    print(res)
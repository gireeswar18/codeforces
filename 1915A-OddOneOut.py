t = int(input())

for i in range(t):
    lt = list(map(int, input().split()))
    res = 0

    for num in lt:
        res = res ^ num
    
    print(res)
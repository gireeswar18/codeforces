t = int(input())

for i in range(t):
    n = int(input())
    lt = list(map(int, input().split()))

    lt = sorted(lt)
    res = "YES"

    for i in range(1, len(lt)):
        if abs(lt[i] - lt[i - 1]) > 1:
            res = "NO"
            break
    
    print(res)
t = int(input())

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


for _ in range(t):
    n = int(input())
    res = 1

    while n > 0:
        curr = gcd(n, n // 2)
        if curr == 1:
            n -= 1
        else:
            res = curr
            break
    
    print(res)
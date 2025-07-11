n, m = map(int, input().split())

def isPrime(num):
    if num < 2: return False
    if num == 2: return True

    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True


for i in range(n + 1, m + 1):
    if isPrime(i):
        print("YES" if i == m else "NO")
        exit()
    
print("NO")
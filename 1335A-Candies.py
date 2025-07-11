t = int(input())
lt = []

for i in range(t):
    lt.append(int(input()))

def helper(n):
    if n < 3:
        print(0)
        return

    if n % 2 == 0:
        print((n // 2) - 1)
    else:
        print(n // 2)

for i in lt:
    helper(i)
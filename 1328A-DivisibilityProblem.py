t = int(input())

def helper(a, b):
    if a % b == 0:
        return 0

    res = a // b

    return ((res + 1) * b) - a

for i in range(t):
    a, b = map(int, input().split())
    print(helper(a, b))
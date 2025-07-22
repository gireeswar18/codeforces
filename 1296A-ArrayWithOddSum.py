t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    odd = 0
    even = 0
    for num in arr:
        if num % 2 == 1:
            odd += 1
        else:
            even += 1

    if odd % 2 == 1 or (odd > 0 and even != 0):
        print("YES")
    else:
        print("NO")
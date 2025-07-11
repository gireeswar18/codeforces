t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    even, odd = 0, 0

    for num in arr:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    
    if odd % 2 == 0:
        print("YES")
    else:
        print("NO")
t = int(input())

for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))
    even = 0
    odd = 0

    for num in arr:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    if even == odd:
        print("Yes")
    else:
        print("No")
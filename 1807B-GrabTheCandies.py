t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    even_sum = 0
    odd_sum = 0

    for num in arr:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    if even_sum > odd_sum:
        print("YES")
    else:
        print("NO")
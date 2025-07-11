t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    curr_zero = 0
    max_zero = 0

    for i in range(n):
        if arr[i] == 1:
            max_zero = max(max_zero, curr_zero)
            curr_zero = 0
        else:
            curr_zero += 1

    max_zero = max(max_zero, curr_zero)
    print(max_zero)
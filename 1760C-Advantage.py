t = int(input())

for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    # find max and second max
    f_max = 0
    s_max = 0

    for i in range(n):
        if arr[i] > f_max:
            s_max = f_max
            f_max = arr[i]
            
        elif arr[i] > s_max:
            s_max = arr[i]

    for i in range(n):
        if arr[i] == f_max:
            print(arr[i] - s_max, end = " ")
        else:
            print(arr[i] - f_max, end = " ")
    print()
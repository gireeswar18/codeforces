t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))

    # find the first and second max
    # check with the final players skill

    fmax = -1
    smax = -1

    for num in arr:
        if num > fmax:
            smax = fmax
            fmax = num
        elif num > smax:
            smax = num

    final_p1 = max(arr[0], arr[1])
    final_p2 = max(arr[2], arr[3])

    if (final_p1 == fmax or final_p1 == smax) and (final_p2 == fmax or final_p2 == smax):
        print("YES")
    else:
        print("NO")
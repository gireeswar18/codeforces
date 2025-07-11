t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))

    min_num = a[0]
    min_ind = 0
    product = 1

    for i, num in enumerate(a):
        if num < min_num:
            min_num = num
            min_ind = i

    for i, num in enumerate(a):
        if i != min_ind:
            product *= num

    print(product * (min_num + 1))
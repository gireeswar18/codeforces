t = int(input())

for _ in range(t):
    n = int(input())

    if n == 2:
        print(2)
        continue

    sum1 = 0
    sum2 = 0

    num = 2

    arr = []

    for i in range(n):
        arr.append(num)
        num = num << 1

    for i in range((n // 2) - 1):
        sum1 += arr[i]

    sum1 += arr[-1]

    for i in range((n // 2) - 1, n - 1):
        sum2 += arr[i]

    # print(sum1)
    # print(sum2)
    # print(arr)

    print(sum1 - sum2)
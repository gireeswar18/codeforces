
'''

4 6 3

inserting num should be, < 4 and < 6
so min(4, 6) < insert_num
min = 4, so -> 3

min = 3, so -> 2 

'''

t = int(input())

for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))
    res = [arr[0]]

    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            res.append(1)
        res.append(arr[i])

    print(len(res))
    for num in res:
        print(num, end=" ")
    print()
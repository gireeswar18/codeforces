t = int(input())

for i in range(t):
    a, b, c = map(int, input().split())

    if (a > b or a > c) and (a < b or a < c):
        print(a)
    elif (b > a or b > c) and (b < a or b < c):
        print(b)
    else:
        print(c)
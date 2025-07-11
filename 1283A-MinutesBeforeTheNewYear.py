t = int(input())

for _ in range(t):
    h, m = map(int, input().split())

    total = 1440

    curr_time = h * 60 + m

    print(total - curr_time)
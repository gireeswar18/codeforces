t = int(input())

for _ in range(t):
    m, a, b, c = map(int, input().split())

    first_row = m
    second_row = m
    seats = 0

    take = min(first_row, a)
    seats += take
    first_row -= take

    take = min(second_row, b)
    seats += take
    second_row -= take

    take = min(first_row, c)
    seats += take
    c -= take
    first_row -= take

    take = min(second_row, c)
    seats += take
    second_row -= take

    print(seats)
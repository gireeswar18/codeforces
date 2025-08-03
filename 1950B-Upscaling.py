t = int(input())

for _ in range(t):
    n = int(input())

    is_dot = False
    row_1 = []
    row_2 = []

    for i in range(n):
        if is_dot:
            row_1.append('.')
            row_1.append('.')
            row_2.append('#')
            row_2.append('#')
        else:
            row_1.append('#')
            row_1.append('#')
            row_2.append('.')
            row_2.append('.')

        is_dot = not is_dot

    r1 = "".join(row_1)
    r2 = "".join(row_2)

    for i in range(n):
        if i % 2 == 0:
            print(r1)
            print(r1)
        else:
            print(r2)
            print(r2)
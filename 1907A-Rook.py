t = int(input())

for _ in range(t):
    curr_pos = str(input())

    col = curr_pos[0]
    row = curr_pos[1]

    for r in range(1, 9):
        pos = col + str(r)
        if pos != curr_pos:
            print(pos)

    for c in range(0, 8):
        pos = chr(ord('a') + c) + str(row)
        if pos != curr_pos:
            print(pos)

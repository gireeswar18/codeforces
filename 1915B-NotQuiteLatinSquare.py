t = int(input())

for _ in range(t):
    mat = []
    for _ in range(3):
        word = str(input())
        mat.append(word)

    for row in mat:
        for c in row:
            if c == '?':
                letters = set(row)
                if 'A' not in letters:
                    print('A')
                elif 'B' not in letters:
                    print('B')
                else:
                    print('C')
                    break
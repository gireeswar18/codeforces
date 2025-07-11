t = int(input())

for _ in range(t):
    matrix = []
    res = []

    r = -1
    c = -1

    for _ in range(8):
        string = str(input())
        matrix.append(string)

    
    for i in range(8):
        for j in range(8):
            if matrix[i][j] != '.':
                r = i
                c = j
                break

        if r != -1:
            break
        
    for i in range(r, 8):
        if matrix[i][c] == '.':
            break
            
        res.append(matrix[i][c])

    print("".join(res))
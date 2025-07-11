'''
    BGGBG

    t = 1 -> GBGGB

    x -> boy, y -> girl

    loop until n - 1
    x = B, y = G, swap, move 2 steps
    x = G -> move 1 step

'''

n, t = map(int, input().split())

word = str(input())
q = list(word)

while t != 0:
    i = 0
    while i < n - 1:
        x, y = q[i], q[i + 1]

        if x == 'B' and y == 'G':
            q[i], q[i + 1] = q[i + 1], q[i]
            i += 1
        
        i += 1
    t -= 1

print("".join(q))

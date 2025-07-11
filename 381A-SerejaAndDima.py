n = int(input())

lt = list(map(int, input().split()))

s, d = 0, 0
ser_turn = True

l, r = 0, n - 1

while l <= r:
    if ser_turn:
        if lt[l] > lt[r]:
            s += lt[l]
            l += 1
        else:
            s += lt[r]
            r -= 1
        ser_turn = False
    else:
        if lt[l] > lt[r]:
            d += lt[l]
            l += 1
        else:
            d += lt[r]
            r -= 1
        ser_turn = True

print(s, d)
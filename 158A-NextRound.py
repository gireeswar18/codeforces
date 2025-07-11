n, k = map(int, input().split())
pts = list(map(int, input().split()))

'''
    10 9 8 7 7 7 5 5
    0  1 2 3 4 5 6 7
'''

ind = k - 1
val = pts[ind]

if val == 0:
    i = 0
    while i < ind and pts[i] != 0:
        i += 1
    print(i)
    exit()

while ind < n and pts[ind] == val:
    ind += 1

print(ind)

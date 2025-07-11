n = int(input())

m, c = 0, 0

for i in range(n):
    a, b = map(int, input().split())

    if a > b:
        m += 1
    if b > a:
        c += 1

if m > c:
    print("Mishka")
elif c > m:
    print("Chris")
else:
    print("Friendship is magic!^^")
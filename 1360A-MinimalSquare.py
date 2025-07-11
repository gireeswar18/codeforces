t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    side1 = max(2 * a, b)
    side2 = max(a, 2 * b)

    print(min(side1, side2) ** 2)
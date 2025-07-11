t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())
    res = 0

    # using promotion cost
    reduced_cost = (n // 2) * b
    if n % 2 != 0:
        reduced_cost += a
    
    # using actual cost
    actual_cost = n * a

    print(min(reduced_cost, actual_cost))
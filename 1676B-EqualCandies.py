t = int(input())

for _ in range(t):
    n = int(input())
    candies = list(map(int, input().split()))

    candy_to_be_filled = min(candies)
    candies_to_eat = 0

    for candy in candies:
        candies_to_eat += (candy - candy_to_be_filled)
    
    print(candies_to_eat)
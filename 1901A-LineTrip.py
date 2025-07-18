t = int(input())

for _ in range(t):
    n, dest = map(int, input().split())

    gas_stations = list(map(int, input().split()))

    max_tank = 0

    for i in range(1, n):
        max_tank = max(max_tank, gas_stations[i] - gas_stations[i - 1])
    
    max_tank = max(max_tank, gas_stations[0])
    max_tank = max(max_tank, (dest - gas_stations[-1]) * 2)

    print(max_tank)
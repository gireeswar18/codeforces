'''

- get the stops
- each stop x passengers exit & y passengers enter
- after this calculate the max of passengers in the bus

'''

stops = int(input())

minSeats = 0
passengerCnt = 0

for i in range(stops):
    leave, enter = map(int, input().split())
    
    passengerCnt -= leave
    passengerCnt += enter

    minSeats = max(minSeats, passengerCnt)

print(minSeats)
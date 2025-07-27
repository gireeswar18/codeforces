t = int(input())

for _ in range(t):
    time = str(input())

    hrs = int(time[:2])
    mts = time[3:]

    is_pm = False

    if hrs == 12:
        is_pm = True
    elif hrs == 0:
        hrs = 12
    elif hrs > 12:
        hrs = hrs % 12
        is_pm = True
    
    if hrs < 10:
        hrs = '0' + str(hrs)
    
    print(f"{hrs}:{mts} {'PM' if is_pm else 'AM'}")
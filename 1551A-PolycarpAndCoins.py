t = int(input())

for _ in range(t):
    n = int(input())

    one, two = 0, 0

    # get one rupee coins
    one = n // 3
    rem = n - one

    # check remaining can be made with 2 rupees or not
    # if possible divide the rem by 2
    # else add one to one and sub one to rem
    if rem % 2 == 0:
        two = rem // 2
    else:
        one += 1
        two = (rem - 1) // 2

    print(one, two)
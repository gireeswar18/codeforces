t = int(input())

for i in range(t):
    answered_call = int(input())

    last_digit = answered_call % 10

    total_presses = last_digit * 10

    if (answered_call % 1111 == 0):
        print(total_presses)
    elif (answered_call % 111 == 0):
        print(total_presses - 4)
    elif (answered_call % 11 == 0):
        print(total_presses - 7)
    else:
        print(total_presses - 9)
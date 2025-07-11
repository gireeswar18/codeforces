dollars = int(input())

denominations = [1, 5, 10, 20, 100]
ind = 4

bill = 0

while dollars != 0:
    if dollars < denominations[ind]:
        ind -= 1
    else:
        bill += (dollars // denominations[ind])
        dollars = dollars % denominations[ind]

print(bill)
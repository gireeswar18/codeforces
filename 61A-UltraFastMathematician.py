num1 = str(input())
num2 = str(input())

res = []

for x, y in zip(num1, num2):
    if x != y:
        res.append('1')
    else:
        res.append('0')

print("".join(res))
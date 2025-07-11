year = int(input())

uniq = set()

while True:
    year += 1
    if len(set(str(year))) == 4:
        break

print(year)
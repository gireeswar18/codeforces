username = str(input())
uniq = set(username)

if len(uniq) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
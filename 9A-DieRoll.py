w, y = map(int, input().split())

high = max(w, y)

res = 6 - high

lt = ["1/6", "1/3", "1/2", "2/3", "5/6", "1/1"]

print(lt[res])
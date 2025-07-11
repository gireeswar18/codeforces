n = int(input())

lt = list(map(int, input().split()))

print("EASY" if sum(lt) == 0 else "HARD")
t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    min_turns = min(a, b)
    a -= min_turns
    b -= min_turns

    if a == b:
        print("First" if c % 2 == 1 else "Second")
    else:
        print("First" if a > b else "Second")
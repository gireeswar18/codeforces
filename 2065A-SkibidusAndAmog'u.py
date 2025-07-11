t = int(input())

for _ in range(t):
    singular = str(input())

    print(singular[: len(singular) - 2] + "i")
string = str(input())

rotations = 0
curr = 'a'

for c in string:
    clockwise = abs(ord(c) - ord(curr))
    counter_clockwise = 26 - clockwise

    rotations += min(clockwise, counter_clockwise)
    curr = c

print(rotations)
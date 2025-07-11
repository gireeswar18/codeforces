cubes = int(input())

total_used = 0
prev_level = 0
level = 1

while total_used + (level + prev_level) <= cubes:
    total_used += (level + prev_level)
    prev_level = (level + prev_level)
    level += 1

print(level - 1)
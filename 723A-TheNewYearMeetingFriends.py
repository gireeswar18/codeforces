x, y, z = map(int, input().split())

to_x = abs(x - y) + abs(x - z)
to_y = abs(x - y) + abs(y - z)
to_z = abs(x - z) + abs(y - z)

print(min(to_x, to_y, to_z))
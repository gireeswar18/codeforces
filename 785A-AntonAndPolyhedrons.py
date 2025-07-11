mp = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
}

cubes = int(input())

sides = 0

for i in range(cubes):
    shape = str(input())
    sides += mp[shape]

print(sides)
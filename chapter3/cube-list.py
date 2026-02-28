first_10_cubes = [value**3 for value in range(1, 11)]
for cube in first_10_cubes:
    print(cube)

print("\n the first 3 cubes are:")
for cube in first_10_cubes[:3]:
    print(cube)

print("\n the middle 3 cubes are:")
for cube in first_10_cubes[3:6]:
    print(cube)

print("\n the last 3 cubes are:")
for cube in first_10_cubes[-3:]:
    print(cube)
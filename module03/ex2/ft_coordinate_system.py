#!/usr/bin/env python3

import math

print("=== Game Coordinate System ===")

position = (10, 20, 5)
print("\nPosition created:", position)

origin = (0, 0, 0)

distance = math.sqrt(
    (position[0] - origin[0]) ** 2 +
    (position[1] - origin[1]) ** 2 +
    (position[2] - origin[2]) ** 2
)

print("Distance between", origin, "and", position, ":", round(distance, 2))

coords = "3,4,0"
print('\nParsing coordinates: "3,4,0"')

parts = coords.split(",")

x = int(parts[0])
y = int(parts[1])
z = int(parts[2])

parsed_position = (x, y, z)

print("Parsed position:", parsed_position)

distance2 = math.sqrt(x**2 + y**2 + z**2)

print("Distance between", origin, "and", parsed_position, ":", distance2)

print('\nParsing invalid coordinates: "abc,def,ghi"')

try:
    bad = "abc,def,ghi".split(",")
    x = int(bad[0])
    y = int(bad[1])
    z = int(bad[2])
except Exception as e:
    print("Error parsing coordinates:", e)

print("\nUnpacking demonstration:")

x, y, z = parsed_position

print(f"Player at x={x}, y={y}, z={z}")
print(f"Coordinates: X={x}, Y={y}, Z={z}")
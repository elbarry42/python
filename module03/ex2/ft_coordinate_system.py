#!/usr/bin/env python3

import sys
import math

print("=== Game Coordinate System ===")

# Create a fixed position
position = (10, 20, 5)
print("Position created:", position)

# Origin point
origin = (0, 0, 0)

# Unpack coordinates
x1, y1, z1 = origin
x2, y2, z2 = position

# Distance calculation
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
print("Distance between", origin, "and", position, ":", round(distance, 2))

# Parsing coordinates
coords_string = "3,4,0"
print("\nParsing coordinates:", '"' + coords_string + '"')

try:
    parts = coords_string.split(",")
    x = int(parts[0])
    y = int(parts[1])
    z = int(parts[2])

    parsed_position = (x, y, z)
    print("Parsed position:", parsed_position)

    # Distance from origin
    x2, y2, z2 = parsed_position
    distance = math.sqrt((x2)**2 + (y2)**2 + (z2)**2)

    print("Distance between", origin, "and", parsed_position, ":", distance)

except Exception as e:
    print("Error parsing coordinates:", e)

# Parsing invalid coordinates
invalid_string = "abc,def,ghi"
print("\nParsing invalid coordinates:", '"' + invalid_string + '"')

try:
    parts = invalid_string.split(",")
    x = int(parts[0])
    y = int(parts[1])
    z = int(parts[2])
except Exception as e:
    print("Error parsing coordinates:", e)
    print("Error details - Type:", type(e).__name__, ", Args:", e.args)

# Tuple unpacking demonstration
print("\nUnpacking demonstration:")

position = (3, 4, 0)
x, y, z = position

print(f"Player at x={x}, y={y}, z={z}")
print(f"Coordinates: X={x}, Y={y}, Z={z}")
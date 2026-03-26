#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coords = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = coords.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(parts[0])
            y = float(parts[1])
            z = float(parts[2])
        except ValueError as e:
            print(f"Error: {e}")
            continue

        return x, y, z


print("=== Game Coordinate System ===")

print("\nGet a first set of coordinates")
pos1 = get_player_pos()

print(f"Got a first tuple: {pos1}")

x, y, z = pos1
print(f"It includes: X={x}, Y={y}, Z={z}")

distance = math.sqrt(x ** 2 + y ** 2 + z ** 2)
print(f"Distance to center: {round(distance, 4)}")

print("\nGet a second set of coordinates")
pos2 = get_player_pos()

x1, y1, z1 = pos1
x2, y2, z2 = pos2

distance = math.sqrt(
    (x2 - x1) ** 2 +
    (y2 - y1) ** 2 +
    (z2 - z1) ** 2
)

print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")

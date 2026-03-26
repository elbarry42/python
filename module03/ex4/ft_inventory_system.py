#!/usr/bin/env python3

import sys

print("=== Inventory System Analysis ===")

inventory = {}

for arg in sys.argv[1:]:

    if ":" not in arg:
        print(f"Error - invalid parameter '{arg}'")
        continue

    item, value = arg.split(":", 1)

    if item in inventory:
        print(f"Redundant item '{item}' - discarding")
        continue

    try:
        quantity = int(value)
    except ValueError as e:
        print(f"Quantity error for '{item}': {e}")
        continue

    inventory[item] = quantity


if len(inventory) == 0:
    print("No valid items provided.")
    sys.exit()

print(f"Got inventory: {inventory}")

items = list(inventory.keys())
print(f"Item list: {items}")

total = sum(inventory.values())
print(f"Total quantity of the {len(items)} items: {total}")

for item, quantity in inventory.items():
    percent = (quantity / total) * 100
    print(f"Item {item} represents {percent:.1f}%")

most = max(inventory, key=lambda k: inventory[k])
least = min(inventory, key=lambda k: inventory[k])

print(f"Item most abundant: {most} with quantity {inventory[most]}")
print(f"Item least abundant: {least} with quantity {inventory[least]}")

inventory.update({"magic_item": 1})
print(f"Updated inventory: {inventory}")

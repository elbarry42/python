#!/usr/bin/env python3

import sys

print("=== Inventory System Analysis ===")

inventory = dict()

# Parse command line arguments
for arg in sys.argv[1:]:
    parts = arg.split(":")
    item = parts[0]
    quantity = int(parts[1])
    inventory.update({item: quantity})

# Total items
total_items = sum(inventory.values())
unique_items = len(inventory)

print("Total items in inventory:", total_items)
print("Unique item types:", unique_items)

print("\n=== Current Inventory ===")

# Display inventory with percentage
for item, quantity in inventory.items():
    percentage = (quantity / total_items) * 100
    print(f"{item}: {quantity} units ({percentage:.1f}%)")

print("\n=== Inventory Statistics ===")

# Most and least abundant
most_item = max(inventory, key=inventory.get)
least_item = min(inventory, key=inventory.get)

print(f"Most abundant: {most_item} ({inventory.get(most_item)} units)")
print(f"Least abundant: {least_item} ({inventory.get(least_item)} units)")

print("\n=== Item Categories ===")

moderate = dict()
scarce = dict()

for item, quantity in inventory.items():
    if quantity >= 5:
        moderate[item] = quantity
    else:
        scarce[item] = quantity

print("Moderate:", moderate)
print("Scarce:", scarce)

print("\n=== Management Suggestions ===")

restock = []

for item, quantity in inventory.items():
    if quantity <= 1:
        restock.append(item)

print("Restock needed:", ", ".join(restock))

print("\n=== Dictionary Properties Demo ===")

print("Dictionary keys:", ", ".join(inventory.keys()))
print("Dictionary values:", ", ".join(str(v) for v in inventory.values()))

print("Sample lookup - 'sword' in inventory:", "sword" in inventory)
#!/usr/bin/env python3

print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

print("\nCRISIS ALERT: Attempting access to 'lost_archive.txt'...")
try:
    with open("lost_archive.txt", "r") as file:
        file.read()
except FileNotFoundError:
    print("RESPONSE: Archive not found in storage matrix")
print("STATUS: Crisis handled, system stable")

print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'...")
try:
    raise PermissionError
    with open("classified_vault.txt", "r") as file:
        file.read()
except PermissionError:
    print("RESPONSE: Security protocols deny access")
print("STATUS: Crisis handled, security maintained")

print("\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
try:
    with open("standard_archive.txt", "r") as file:
        content = file.read()
        print(f'SUCCESS: Archive recovered - "{content}"')
    print("STATUS: Normal operations resumed")
except Exception as e:
    print(f"ERROR {e}")

print("\nAll crisis scenarios handled successfully. Archives secure.")

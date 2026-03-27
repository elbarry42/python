#!/usr/bin/env python3

print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

file = None
try:
    print("\nAccessing Storage Vault: ancient_fragment.txt")
    file = open("ancient_fragment.txt", "r")
    print("Connection established...")
    content = file.read()
    print("\nRECOVERED DATA:")
    print(content)
    print("\nData recovery complete. Storage unit disconnected.")
except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")
finally:
    if file:
        file.close()

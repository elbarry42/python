#!/usr/bin/env python3

print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

file = None

try:
    print("\nInitializing new storage unit: new_discovery.txt")
    file = open("new_discovery.txt", "w")
    print("Storage unit created successfully...")
    print("\nInscribing preservation data...")

    entry1 = "[ENTRY 001] New quantum algorithm discovered\n"
    entry2 = "[ENTRY 002] Efficiency increased by 347%\n"
    entry3 = "[ENTRY 003] Archived by Data Archivist trainee\n"

    file.write(entry1)
    file.write(entry2)
    file.write(entry3)

    print(entry1, end="")
    print(entry2, end="")
    print(entry3, end="")

    print("\nData inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")
except Exception:
    print("ERROR")
finally:
    if file:
        file.close()

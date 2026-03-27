#!/usr/bin/env python3

print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")

try:
    print("\nInitiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    print("\nSECURE EXTRACTION:")
    with open("classified_data.txt", "r") as file:
        content = file.read()
        print(content)

    print("\nSECURE PRESERVATION:")
    entry = "[CLASSIFIED] New security protocols archived"
    with open("security_protocols.txt", "w") as file:
        file.write(entry)
        print(entry)
    print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")
except Exception as e:
    print(f"ERROR {e}")

#!/usr/bin/env python3

import sys

print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

archivist_id = input("\nInput Stream active. Enter archivist ID: ")
status = input("Input Stream active. Enter status report: ")

sys.stdout.write(
    f"\n[STANDARD] Archive status from {archivist_id}: {status}\n"
)
sys.stderr.write(
    "[ALERT] System diagnostic: Communication channels verified\n"
)
sys.stdout.write("[STANDARD] Data transmission complete\n")

sys.stdout.write("\nThree-channel communication test successful.")

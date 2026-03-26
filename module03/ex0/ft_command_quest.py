#!/usr/bin/env python3

import sys

print("=== Command Quest ===")

if len(sys.argv) == 1:
    print("No arguments provided!")
    print("Program name:", sys.argv[0])
    print("Total arguments:", len(sys.argv))
else:
    print("Program name:", sys.argv[0])
    print("Arguments received:", len(sys.argv) - 1)

    for i in range(1, len(sys.argv)):
        print("Argument", i, ":", sys.argv[i])

    print("Total arguments:", len(sys.argv))

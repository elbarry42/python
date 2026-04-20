#!/usr/bin/env python3

import sys
import os
import site


def is_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


def get_venv_name() -> str:
    return os.path.basename(sys.prefix)


def print_outside_env() -> None:
    print("\nMATRIX STATUS: You're still plugged in")
    print(f"\nCurrent Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")

    print("\nTo enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env\\Scripts\\activate   # On Windows")
    print("\nThen run this program again.")


def print_inside_env() -> None:
    venv_name = get_venv_name()

    print("\nMATRIX STATUS: Welcome to the construct")
    print(f"\nCurrent Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {sys.prefix}")
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.\n")

    print("\nPackage installation path:")

    try:
        paths = site.getsitepackages()
        for path in paths:
            print(path)
    except AttributeError:
        # fallback pour certains environnements
        print(site.getusersitepackages())


def main() -> None:
    if is_virtual_env():
        print_inside_env()
    else:
        print_outside_env()


if __name__ == "__main__":
    main()

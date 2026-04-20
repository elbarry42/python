#!/usr/bin/env python3

import sys
import importlib


def check_package(name: str):
    try:
        module = importlib.import_module(name)
        return module
    except ImportError:
        return None


def print_status(name: str, module) -> None:
    if module:
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {name} ({version}) - Ready")
    else:
        print(f"[ERROR] {name} - Not installed")


def install_instructions() -> None:
    print("\nTo install dependencies:")
    print("Using pip:")
    print("pip install -r requirements.txt\n")

    print("Using Poetry:")
    print("poetry install")
    print("poetry run python loading.py")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    pandas = check_package("pandas")
    numpy = check_package("numpy")
    matplotlib = check_package("matplotlib")
    requests = check_package("requests")

    print_status("pandas", pandas)
    print_status("numpy", numpy)
    print_status("matplotlib", matplotlib)
    if requests:
        print_status("requests", requests)

    if not pandas or not numpy or not matplotlib:
        print("\nMissing required dependencies.")
        install_instructions()
        sys.exit(1)

    # Imports réels après vérification
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")

    data = np.random.randn(1000)

    print("Processing 1000 data points...")

    # Analyse avec pandas
    df = pd.DataFrame(data, columns=["values"])

    mean = df["values"].mean()
    std = df["values"].std()

    print(f"Mean: {mean:.2f}")
    print(f"Std: {std:.2f}")

    print("\nGenerating visualization...")

    # Graph
    plt.figure()
    df["values"].plot(title="Matrix Data Distribution")
    plt.savefig("matrix_analysis.png")

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()

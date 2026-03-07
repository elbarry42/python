def garden_operations() -> None:
    print("\nTesting ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("\nTesting ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    print("\nTesting FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    print("\nTesting KeyError...")
    try:
        plants = {"tomato": 10}
        print(plants["lettuce"])
    except KeyError:
        print("Caught KeyError: 'lettuce'")

    print("\nTesting multiple errors together...")
    try:
        int("abc")
    except (ValueError, TypeError):
        print("Caught an error, but program continues!")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()

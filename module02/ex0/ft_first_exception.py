def check_temperature(temp_str: str) -> None:
    try:
        temp = int(temp_str)

        if temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        elif temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!")

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    tests = ["25", "abc", "100", "-50"]

    for t in tests:
        print(f"Testing temperature: {t}")
        check_temperature(t)
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()

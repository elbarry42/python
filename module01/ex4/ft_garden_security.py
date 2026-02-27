#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name: str = name
        self._height: int = 0
        self._age: int = 0

        if height >= 0:
            self._height = height
        else:
            print("Security: Negative height rejected at creation")

        if age >= 0:
            self._age = age
        else:
            print("Security: Negative age rejected at creation")

    def set_height(self, new_h: int) -> None:
        if new_h >= 0:
            self._height = new_h
            print(f"Height updated: {self._height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {new_h}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, new_a: int) -> None:
        if new_a >= 0:
            self._age = new_a
            print(f"Age updated: {self._age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {new_a} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_name(self) -> str:
        return self._name


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 10, 5)
    print(f"Plant created: {rose.get_name()}")
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    print()
    print(
        f"Current plant: {rose.get_name()} "
        f"({rose.get_height()}cm, {rose.get_age()} days)"
    )

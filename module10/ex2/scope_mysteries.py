#!/usr/bin/env python3

from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count

        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:

    total_power = initial_power

    def accumulator(amount: int) -> int:

        nonlocal total_power

        total_power += amount

        return total_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:

    def enchant(item_name: str) -> str:
        return (f"{enchantment_type} {item_name}")
    return enchant


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value) -> None:

        memory[key] = value

    def recall(key: str):

        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")

    counter_a = mage_counter()
    counter_b = mage_counter()

    print(counter_a())
    print(counter_a())
    print(counter_b())

    print("\nTesting spell accumulator...")

    accumulator = spell_accumulator(100)

    print(accumulator(20))
    print(accumulator(30))

    print("\nTesting enchantment factory...")

    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")

    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")

    vault = memory_vault()

    vault["store"]("secret", 42)

    print(vault["recall"]("secret"))
    print(vault["recall"]("unknown"))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3


from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
from typing import Any
import operator


def spell_reducer(spells: list[int], operation: str) -> int:

    if not spells:
        return 0

    operations: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if operation not in operations:
        raise ValueError(
            "Unknown operation"
        )
    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:

    return {
        "fire": partial(
            base_enchantment,
            50,
            "fire"
        ),

        "ice": partial(
            base_enchantment,
            50,
            "ice"
        ),

        "lightning": partial(
            base_enchantment,
            50,
            "lightning"
        )
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:

    if n < 2:
        return n
    return (memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2))


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def dispatch(spell) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(spell: int) -> str:
        return (f"Damage spell: {spell} damage")

    @dispatch.register
    def _(spell: str) -> str:
        return (f"Enchantment: {spell}")

    @dispatch.register
    def _(spell: list) -> str:
        return (f"Multi-cast: {len(spell)} spells")
    return dispatch


def enchantment(power: int, element: str, target: str) -> str:
    return (f"{element} enchantment on {target} with {power} power")


def main() -> None:
    print("Testing spell reducer...")

    spells = [10, 20, 30, 40]

    print("Sum:", spell_reducer(spells, "add"))

    print("Product:", spell_reducer(spells, "multiply"))

    print("Max:", spell_reducer(spells, "max"))

    print("\nTesting partial enchanter...")

    enchantments = partial_enchanter(enchantment)

    print(enchantments["fire"]("Dragon"))

    print(enchantments["ice"]("Knight"))

    print("\nTesting fibonacci...")

    print(memoized_fibonacci(10))

    print(memoized_fibonacci(15))

    print(memoized_fibonacci.cache_info())

    print("\nTesting dispatcher...")

    dispatcher = spell_dispatcher()

    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))
    print(dispatcher(3.14))


if __name__ == "__main__":
    main()

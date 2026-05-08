#!/usr/bin/env python3


from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:

    def combined(target: str, power: int) -> tuple[str, str]:

        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:

    def amplified(target: str, power: int) -> str:

        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:

    def conditional_spell(target: str, power: int) -> str:

        if condition(target, power):
            return spell(target, power)

        return "Spell fizzled"
    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:

    def sequence(target: str, power: int) -> list[str]:

        return [
            spell(target, power)
            for spell in spells
        ]
    return sequence


def fireball(target: str, power: int) -> str:
    return (f"Fireball hits {target} for {power} damage")


def heal(target: str, power: int) -> str:
    return (f"Heal restores {target} for {power} HP")


def shield(target: str, power: int) -> str:
    return (f"Shield protects {target} with {power} armor")


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)

    print(combined("Dragon", 20))

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(
        fireball,
        3
    )

    print(mega_fireball("Dragon", 10))

    print("\nTesting conditional caster...")

    def strong_enough(target: str, power: int) -> bool:
        return power >= 20

    safe_spell = conditional_caster(strong_enough, fireball)

    print(safe_spell("Dragon", 10))
    print(safe_spell("Dragon", 25))

    print("\nTesting spell sequence...")

    combo = spell_sequence([fireball, heal, shield])

    results = combo("Knight", 15)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2.strategies import (
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
)


def battle(opponents):
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):

            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            c1 = factory1.create_base()
            c2 = factory2.create_base()

            print("\n* Battle *")
            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")

            try:
                strategy1.act(c1)
                strategy2.act(c2)

            except ValueError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main():
    flame = FlameFactory()
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    normal = NormalStrategy()
    defensive = DefensiveStrategy()
    aggressive = AggressiveStrategy()

    print("Tournament 0 (basic)")
    battle([
        (flame, normal),
        (healing, defensive),
    ])

    print("\nTournament 1 (error)")
    battle([
        (flame, aggressive),  # ❌ erreur
        (healing, defensive),
    ])

    print("\nTournament 2 (multiple)")
    battle([
        (AquaFactory(), normal),
        (healing, defensive),
        (transform, aggressive),
    ])


if __name__ == "__main__":
    main()

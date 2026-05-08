#!/usr/bin/env python3


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {
            "max_power": 0,
            "min_power": 0,
            "avg_power": 0.0
        }

    return {
        "max_power": max(
            mages,
            key=lambda mage: mage["power"]
        )["power"],

        "min_power": min(
            mages,
            key=lambda mage: mage["power"]
        )["power"],

        "avg_power": round(
            sum(
                mage["power"]
                for mage in mages
            ) / len(mages),
            2
        )
    }


def main() -> None:
    print("Testing artifact sorter...")
    artifacts = [
        {
            "name": "Crystal Orb",
            "power": 85,
            "type": "magic"
        },
        {
            "name": "Fire Staff",
            "power": 92,
            "type": "weapon"
        },
        {
            "name": "Shadow Dagger",
            "power": 70,
            "type": "weapon"
        }
    ]

    sorted_artifacts = artifact_sorter(artifacts)

    for artifact in sorted_artifacts:
        print(
            f"{artifact['name']} "
            f"({artifact['power']} power)"
        )

    print("\nTesting power filter...")
    mages = [
        {
            "name": "Merlin",
            "power": 95,
            "element": "fire"
        },
        {
            "name": "Luna",
            "power": 60,
            "element": "ice"
        },
        {
            "name": "Zephyr",
            "power": 80,
            "element": "wind"
        }
    ]

    filtered_mages = power_filter(mages, 80)

    for mage in filtered_mages:
        print(
            f"{mage['name']} "
            f"({mage['power']} power)"
        )

    print("\nTesting spell transformer...")
    spells = [
        "fireball",
        "heal",
        "shield"
    ]

    transformed_spells = spell_transformer(spells)

    for spell in transformed_spells:
        print(spell)

    print("\nTesting mage stats...")
    stats = mage_stats(mages)

    print(f"Max power: {stats['max_power']}")
    print(f"Min power: {stats['min_power']}")
    print(f"Average power: {stats['avg_power']}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import random

print("=== Achievement Tracker System ===")

all_achievements = [
    "First Steps",
    "Treasure Hunter",
    "Boss Slayer",
    "Master Explorer",
    "Collector Supreme",
    "Speed Runner",
    "Strategist",
    "Untouchable",
    "Survivor",
    "Sharp Mind",
    "Unstoppable",
    "World Savior",
    "Crafting Genius",
    "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    count = random.randint(3, len(all_achievements))
    chosen = random.sample(all_achievements, count)
    return set(chosen)


players = {
    "Alice": gen_player_achievements(),
    "Bob": gen_player_achievements(),
    "Charlie": gen_player_achievements(),
    "Dylan": gen_player_achievements(),
}

print()
for name, achievements in players.items():
    print(f"Player {name}: {achievements}")

all_sets = players.values()

all_unique: set[str] = set()
for s in all_sets:
    all_unique = all_unique.union(s)

print("\nAll distinct achievements:", all_unique)

common = set(all_achievements)

for s in players.values():
    common = common.intersection(s)

print("\nCommon achievements:", common)

print()
for name, achievements in players.items():
    others: set[str] = set()

    for n, a in players.items():
        if n != name:
            others = others.union(a)

    unique = achievements.difference(others)
    print(f"Only {name} has: {unique}")

print()
for name, achievements in players.items():
    missing = set(all_achievements).difference(achievements)
    print(f"{name} is missing: {missing}")

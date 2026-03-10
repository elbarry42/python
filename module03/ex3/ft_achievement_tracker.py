#!/usr/bin/env python3

print("=== Achievement Tracker System ===")

alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
bob = {"first_kill", "level_10", "boss_slayer", "collector"}
charlie = {"level_10", "treasure_hunter", "boss_slayer", "speed_demon", "perfectionist"}

print("\nPlayer alice achievements:", alice)
print("Player bob achievements:", bob)
print("Player charlie achievements:", charlie)

print("\n=== Achievement Analytics ===")

all_achievements = alice.union(bob).union(charlie)
print("All unique achievements:", all_achievements)
print("Total unique achievements:", len(all_achievements))

common = alice.intersection(bob).intersection(charlie)
print("\nCommon to all players:", common)

rare = {"collector", "perfectionist"}
print("Rare achievements (1 player):", rare)

alice_bob_common = alice.intersection(bob)
print("\nAlice vs Bob common:", alice_bob_common)

alice_unique = alice.difference(bob)
print("Alice unique:", alice_unique)

bob_unique = bob.difference(alice)
print("Bob unique:", bob_unique)
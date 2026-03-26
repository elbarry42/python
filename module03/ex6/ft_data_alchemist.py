#!/usr/bin/env python3

import random

print("=== Game Data Alchemist ===")

players = [
    "Alice", "bob", "Charlie", "dylan",
    "Emma", "Gregory", "john", "kevin", "Liam"
]

print(f"\nInitial list of players: {players}")

capitalized = [name.capitalize() for name in players]

print(f"\nNew list with all names capitalized: {capitalized}")

capitalized_only = [
    name for name in players if name[0].isupper()
]

print(f"\nNew list of capitalized names only: {capitalized_only}")

scores = {
    name: random.randint(0, 1000)
    for name in capitalized
}
print(f"\nScore dict: {scores}")

average = sum(scores.values()) / len(scores)
print(f"\nScore average is {average:.2f}")

high_scores = {
    name: score
    for name, score in scores.items()
    if score > average
}
print(f"\nHigh scores: {high_scores}")

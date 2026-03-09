#!/usr/bin/env python3

import sys

print("=== Player Score Analytics ===")

if len(sys.argv) == 1:
    print(
        "No scores provided. Usage:"
        "python3 ft_score_analytics.py <score1> <score2> ..."
    )
    sys.exit()

scores = []

for arg in sys.argv[1:]:
    try:
        score = int(arg)
        scores.append(score)
    except:
        print("Invalid score ignored:", arg)

if len(scores) == 0:
    print("No valid scores provided.")
    sys.exit()

total_players = len(scores)
total_score = sum(scores)
average = total_score / total_players
high = max(scores)
low = min(scores)
score_range = high - low

print("Scores processed:", scores)
print("Total players:", total_players)
print("Total score:", total_score)
print("Average score:", average)
print("High score:", high)
print("Low score:", low)
print("Score range:", score_range)
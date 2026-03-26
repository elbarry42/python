#!/usr/bin/env python3

import random
from typing import Generator, Tuple

print("=== Game Data Stream Processor ===")

players = ["alice", "bob", "charlie", "dylan"]
actions = [
    "run", "eat", "sleep", "grab", "move", "climb", "swim", "use", "release"
]


def get_event() -> Generator[Tuple[str, str], None, None]:
    for _ in range(1000):
        player = random.choice(players)
        action = random.choice(actions)
        yield player, action


for i, (player, action) in enumerate(get_event()):
    print(f"Event {i}: Player {player} did action {action}")

event_list: list[tuple[str, str]] = []

for _ in range(10):
    player = random.choice(players)
    action = random.choice(actions)
    event_list.append((player, action))

print(f"Built list of 10 events: {event_list}")

while event_list:
    event = event_list.pop()
    print(f"Got event from list: {event}")
    print(f"Remains in list: {event_list}")

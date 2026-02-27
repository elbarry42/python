#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self) -> None:
        self.height = self.height + 1

    def age_one_day(self) -> None:
        self.age = self.age + 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    plants = [rose, sunflower, cactus]

    print("=== Day 1 ===")
    for plant in plants:
        print(plant.get_info())

    initial_height = plant.height

    for _ in range(6):
        for plant in plants:
            plant.grow()
            plant.age_one_day()

    growth = plant.height - initial_height
    print("=== Day 7 ===")
    for plant in plants:
        print(plant.get_info())
    print(f"Growth this week: +{growth}cm")

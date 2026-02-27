#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        print(f"{self.name} (Flower): {self.height}cm, "
              f"{self.age} days, {self.color} color")
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(
        self, name: str, height: int, age: int, diameter: int
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = diameter

    def produce_shade(self) -> None:
        print(f"{self.name} (Tree): {self.height}cm, "
              f"{self.age} days, {self.trunk_diameter}cm diameter")
        shade_area = self.trunk_diameter * 1.56
        print(f"{self.name} provides {shade_area} square meters of shade")


class Vegetable(Plant):
    def __init__(
        self, name: str, height: int, age: int, season: str, nutrition: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = season
        self.nutritional_value: str = nutrition

    def harvest_info(self) -> None:
        print(f"{self.name} (Vegetable): {self.height}cm, "
              f"{self.age} days, {self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 25, 30, "red")
    lily = Flower("Lily", 40, 15, "white")

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 300, 1000, 30)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 15, 60, "autumn", "vitamin A")

    print()
    rose.bloom()
    print()
    oak.produce_shade()
    print()
    tomato.harvest_info()

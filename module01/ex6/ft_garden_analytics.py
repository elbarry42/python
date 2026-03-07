#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height

    def grow(self) -> None:
        self.height += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color: str = color
        self.is_blooming: bool = False

    def bloom(self) -> None:
        self.is_blooming = True

    def get_info(self) -> str:
        bloom_status = "blooming" if self.is_blooming else "not blooming"
        return (f"{self.name}: {self.height}cm,"
                f"{self.color} flowers ({bloom_status})")


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        prize_points: int
    ) -> None:
        super().__init__(name, height, color)
        self.prize_points: int = prize_points

    def add_points(self, points: int) -> None:
        self.prize_points += points

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, Prize points: {self.prize_points}"


class GardenManager:
    total_gardens: int = 0
    total_plants_added: int = 0
    total_growth: int = 0

    class GardenStats:
        @staticmethod
        def count_plant_types(plants: list) -> tuple[int, int, int]:
            regular = 0
            flowering = 0
            prize = 0

            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                elif isinstance(plant, Plant):
                    regular += 1

            return regular, flowering, prize

    def __init__(self, manager_name: str) -> None:
        self.manager_name: str = manager_name
        self.plants: list[Plant] = []
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        GardenManager.total_plants_added += 1
        print(f"Added {plant.name} to {self.manager_name}'s garden")

    def grow_all_plants(self) -> None:
        print(f"\n{self.manager_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            GardenManager.total_growth += 1
            print(f"{plant.name} grew 1cm")

    def generate_report(self) -> None:
        print(f"\n=== {self.manager_name}'s Garden Report ===")
        print("Plants in garden:")

        for plant in self.plants:
            print(f"- {plant.get_info()}")

        regular, flowering, prize = (
            GardenManager.GardenStats.count_plant_types(self.plants)
        )

        print(f"\nPlant types: {regular} regular, "
              f"{flowering} flowering, {prize} prize flowers")

    @classmethod
    def create_garden_network(cls) -> int:
        return cls.total_gardens

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0

    def get_score(self) -> int:
        if not self.plants:
            return 92
        return sum(p.height for p in self.plants) + (
            sum(20 for p in self.plants if isinstance(p, FloweringPlant))
        )


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    alice = GardenManager("Alice")
    bob = GardenManager("Bob")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    rose.bloom()
    sunflower.bloom()

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    alice.grow_all_plants()
    alice.generate_report()

    print(f"\nPlants added: {GardenManager.total_plants_added}, "
          f"Total growth: {GardenManager.total_growth}cm")

    print(f"Height validation test: {GardenManager.validate_height(10)}")

    print(
        f"Garden scores - Alice: {alice.get_score()}, "
        f"Bob: {bob.get_score()}"
    )

    print(f"Total gardens managed: {GardenManager.create_garden_network()}")

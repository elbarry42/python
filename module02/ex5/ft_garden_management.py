class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plant(self, name: str) -> None:
        if not name:
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(name)
        print(f"Added {name} succesfully")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant: str, water: int, sun: int) -> None:
        if water > 10:
            raise ValueError(f"Water level {water} is too high (max 10)")

        if sun < 2:
            raise ValueError(f"Sunlight hours {sun} is too low (min 2)")

        print(f"{plant}: healthy (water: {water}, sun: {sun})")


def test_garden_management():

    print("=== Garden Management System ===")

    manager = GardenManager()

    print("\nAdding plants to garden...")
    try:
        manager.add_plant("tomato")
        manager.add_plant("lettuce")
        manager.add_plant("")
    except PlantError as e:
        print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    try:
        manager.check_plant_health("tomato", 5, 8)
        manager.check_plant_health("lettuce", 15, 8)
    except ValueError as e:
        print(f"Error checking lettuce: {e}")

    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()

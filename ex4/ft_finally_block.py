class PlantError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return f"{self.message}"


def water_plant(plant_name: str) -> None:
    if not plant_name == plant_name.capitalize():
        raise PlantError(f"invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name} : [OK]")


def test_watering_system(plants: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as err_msg:
        print(f"Caught PlantError: {err_msg}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering systems")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    titles = ["valid", "invalid"]
    valid_plants = ["Tomato", "Lettuce", "Carrots"]
    invalid_plants = ["Tomato", "lettuce", "Carrots"]

    for title in titles:
        print(f"\nTesting {title} plants...")
        if title == "valid":
            test_watering_system(valid_plants)
        elif title == "invalid":
            test_watering_system(invalid_plants)
    print("\nCleanup always happens, even with errors!")

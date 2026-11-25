class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)
        self.message = message
        self.plant = PlantError(message)
        self.water = WaterError(message)


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        self.message = message


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        self.message = message


def error(err_no: int) -> None:
    if err_no == 0:
        raise PlantError("the tomato plant is wilting!")
    if err_no == 1:
        raise WaterError("Not enough water in the tank!")
    if err_no == 2:
        raise GardenError("the tomato plant is wilting!")
    if err_no == 3:
        raise GardenError("Not enough water in the tank!")
    print ("toujours la")

def test_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    titles = ["PlantError", "WaterError", "catching all garden errors"]
    x = 0
    for type in titles:
        print(f"\nTesting {type}...")
        try:
            error(x)
        except PlantError as err_mes:
            print(f"caught PlantError: {err_mes}")
        except WaterError as err_mes:
            print(f"caught WaterError: {err_mes}")
        except GardenError as err_mes:
            print(f"caught GardenError: {err_mes}")
            if x == 2:
                try:
                    error(3)
                except GardenError as err_mes2:
                    print(f"caught GardenError: {err_mes2}")
        x += 1
    print("\nAll custom error types work correctly")


if __name__ == "__main__":
    test_errors()

def garden_operations(operation_number: int) -> None:
    if operation_number > 3:
        return
    if operation_number == 0:
        int("abc")
    if operation_number == 1:
        100/0
    if operation_number == 2:
        open("capitalisme_vert.txt")
    if operation_number == 3:
        "abc" + 123


def test_error_types() -> None:
    print("=== Garden Errors Types Demo ===")
    for x in range(5):
        print(f"Testing operation {x}...")
        try:
            garden_operations(x)
        except ValueError as err_mes:
            print(f"Caught ValueError: {err_mes}\n")
        except ZeroDivisionError as err_mes:
            print(f"Caught ZeroDivisionError: {err_mes}\n")
        except FileNotFoundError as err_mes:
            print(f"Caught FileNotFoundError: {err_mes}\n")
        except TypeError as err_mes:
            print(f"Caught TypeError: {err_mes}\n")
        else:
            print("Operation completed sucessfully\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_error_types()

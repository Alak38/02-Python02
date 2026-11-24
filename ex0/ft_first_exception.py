#!/usr/bin/python3

def input_temperature(temp_str: str) -> int:
    return (int(temp_str))


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    input = "25"
    ret = input_temperature(input)
    print(f"Input data is '{input}'")
    print(f"Temperature is now {ret}°C")
    input = "abc"
    print(f"\nInput data is '{input}'")
    try:
        ret = input_temperature(input)
    except Exception as err_mes:
        print(f"Caught input_temperatur error: {err_mes}")
    else:
        print(f"Temperature is now {ret}°C")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()

#!/usr/bin/python3

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise Exception(f"{temp}°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise Exception(f"{temp}°C is too cold for plants (min 0°C)")
    return (temp)


def test_temperature() -> None:
    input_list = ["25", "abc", "100", "-50"]
    print("=== Garden Temperature Checker ===")
    for input in input_list:
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

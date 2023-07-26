
def heating_cooling(actual_temp, desired_temp, target_unit):
    while actual_temp != desired_temp:
        if actual_temp > desired_temp:
            print("Run A/C")
            actual_temp -= 1
        elif actual_temp < desired_temp:
            print("Run heat")
            actual_temp += 1
    print("Standby")
    converted_temp = convert_temp(desired_temp, "C", target_unit)
    print(f"The desired temperature of {desired_temp} degrees Celsius is equivalent to {converted_temp} degrees {target_unit}.")


def convert_temp(temp, from_unit, to_unit):
    if from_unit == "C" and to_unit == "F":
        return (temp * 9/5) + 32
    elif from_unit == "C" and to_unit == "K":
        return temp + 273.15
    elif from_unit == "F" and to_unit == "C":
        return (temp - 32) * 5/9
    elif from_unit == "F" and to_unit == "K":
        return (temp + 459.67) * 5/9
    elif from_unit == "K" and to_unit == "C":
        return temp - 273.15
    elif from_unit == "K" and to_unit == "F":
        return (temp * 9/5) - 459.67
    elif from_unit == to_unit:
        return temp
    else:
        raise ValueError("Invalid unit conversion. Valid units are 'C', 'F', and 'K'.")

# Example usage:
actual_temp = 90
desired_temp = 345
target_unit = "K"

heating_cooling(actual_temp, desired_temp, target_unit)
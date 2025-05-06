def convert_units(value: float, unit_from: str, unit_to: str):
    if unit_from == "kilometers" and unit_to == "meters":
        return value * 1000
    elif unit_from == "meters" and unit_to == "kilometers":
        return value * 0.001
    elif unit_from == "kilogram" and unit_to == "gram":
        return value * 1000
    elif unit_from == "gram" and unit_to == "kilogram":
        return value * 0.001
    else:
        return "conversion not supported"

def main():
    print("Unit Converter")
    print("Welcome To Unit Converter!")
    
    value = float(input("Enter the value you want to convert: "))
    unit_from = input("Enter the unit you want to convert from: ")
    unit_to = input("Enter the unit you want to convert to: ")

    result = convert_units(value, unit_from, unit_to)
    print(f"{value} {unit_from} is equal to {result} {unit_to}")

main()

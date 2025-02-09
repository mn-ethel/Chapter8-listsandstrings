# List of available units
units = ["inches", "yards", "miles", "millimeters", "centimeters", "meters", "kilometers"]

# Conversion factors (1 unit to others)
conversion_table = [
    [1, 1 / 36, 1 / 63360, 25.4, 2.54, 0.0254, 0.0000254],  # inches
    [36, 1, 1 / 1760, 914.4, 91.44, 0.9144, 0.0009144],  # yards
    [63360, 1760, 1, 1.609e+6, 160934, 1609.34, 1.60934],  # miles
    [1 / 25.4, 1 / 914.4, 1 / 1.609e+6, 1, 0.1, 0.001, 0.000001],  # millimeters
    [1 / 2.54, 1 / 91.44, 1 / 160934, 10, 1, 0.01, 0.00001],  # centimeters
    [1 / 0.0254, 1 / 0.9144, 1 / 1609.34, 1000, 100, 1, 0.001],  # meters
    [1 / 0.0000254, 1 / 0.0009144, 1 / 1.60934, 1e+6, 100000, 1000, 1]  # kilometers
]

# User inputs
length = float(input("Enter the length: "))
from_unit = input(
    "Enter the current unit (inches, yards, miles, millimeters, centimeters, meters, kilometers): ").lower()
to_unit = input("Enter the unit to convert to: ").lower()


if from_unit in units and to_unit in units:
    from_index = units.index(from_unit)
    to_index = units.index(to_unit)

    # Conversion
    converted_length = length * conversion_table[from_index][to_index]

    print(f"{length} {from_unit} is equal to {converted_length:.6f} {to_unit}")
else:
    print("Invalid unit entered. Please use a valid unit from the list.")

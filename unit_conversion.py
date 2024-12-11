def convert_units_cli():
    print("Welcome to the Unit Converter!")
    print("Available conversions:")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Kilograms to Pounds")
    print("6. Pounds to Kilograms")

    conversion_choice = input("Enter the number corresponding to your conversion choice (1-6): ")

    conversions = {
        "1": "Kilometers to Miles",
        "2": "Miles to Kilometers",
        "3": "Celsius to Fahrenheit",
        "4": "Fahrenheit to Celsius",
        "5": "Kilograms to Pounds",
        "6": "Pounds to Kilograms"
    }

    if conversion_choice not in conversions:
        print("Invalid choice! Please run the program again.")
        return

    try:
        value = float(input(f"Enter the value to convert ({conversions[conversion_choice]}): "))
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return

    conversion_rates = {
        "Kilometers to Miles": 0.621371,
        "Miles to Kilometers": 1.60934,
        "Celsius to Fahrenheit": lambda c: c * 9 / 5 + 32,
        "Fahrenheit to Celsius": lambda f: (f - 32) * 5 / 9,
        "Kilograms to Pounds": 2.20462,
        "Pounds to Kilograms": 0.453592
    }

    conversion_type = conversions[conversion_choice]
    if conversion_type in ["Celsius to Fahrenheit", "Fahrenheit to Celsius"]:
        result = conversion_rates[conversion_type](value)
    else:
        result = value * conversion_rates[conversion_type]

    print(f"Result: {result:.2f}")
convert_units_cli()

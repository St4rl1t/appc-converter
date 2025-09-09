def convert_amount(input_period, input_amount, output_period):
    """
    Convert an amount per period (app) from one period unit to another. (e.g., 10 per month is 120 per year)

    Parameters:
        input_period (str): The input period unit ('d' for days, 'w' for weeks, 'm' for months, 'y' for years).
        input_amount (float): The amount per period unit. (Accepts strings that can be converted to float.)
        output_period (str): The output period unit ('d', 'w', 'm', or 'y').

    Returns:
        float: The converted amount per output period unit.

    Raises:
        ValueError: If an invalid period unit or amount is provided.
        TypeError: If the input types are incorrect.

    Note: This function assumes:
        - 1 year = 365 days
        - 1 year = 52 weeks
        - 1 year = 12 months
        - Numbers should be rounded to 2 decimal places.
        - String numbers for input_amount are accepted and converted to float.
    """

    # Supported units and their conversions, add more if needed
    supported_units = ['d', 'w', 'm', 'y']
    conversion_factors = {
        'd': 1 / 365,
        'w': 1 / 52,
        'm': 1 / 12,
        'y': 1
    }

    # Input validation
    if not isinstance(input_period, str) or not isinstance(output_period, str):
        raise TypeError("input_period and output_period must be strings.")

    if isinstance(input_amount, str):
        try:
            input_amount = float(input_amount)
        except ValueError:
            raise TypeError(
                "input_amount must be convertible to float.")

    # Amount type check placed after to allow string number conversion
    if not isinstance(input_amount, (int, float)) or isinstance(input_amount, bool):
        raise TypeError("input_amount must be convertible to float.")

    # Check valid period values
    if input_period.lower() not in supported_units or output_period.lower() not in supported_units:
        raise ValueError("Invalid period. Please enter 'd', 'w', 'm', or 'y'.")
    # End of input validation

    # Conversion logic
    year_am = 0.0  # Initialize variable to prevent pyright from complaining

    if input_period.lower() == output_period.lower():
        # Unecessary sass
        print("It's not a conversion if you don't change the period...")
        return round(input_amount, 2)

    # Convert input amount to years
    year_am = input_amount * (1 / conversion_factors[input_period.lower()])

    # Convert from years to desired output period
    return round(year_am * conversion_factors[output_period.lower()], 2)
    # End of conversion logic


if __name__ == "__main__":
    # Main loop for user input
    while True:
        input_period = input("Enter input period (d/w/m/y): ")
        input_amount = input(f"Enter input amount in {input_period} units: ")
        output_period = input("Enter desired output period (d/w/m/y): ")
        try:
            output_am = convert_amount(
                input_period, input_amount, output_period)
            print(f"Converted amount for {output_period} period: {output_am}")
        except (ValueError, TypeError) as e:
            print(e)
            continue

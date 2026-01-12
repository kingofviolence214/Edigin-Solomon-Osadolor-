# Define tax brackets and rates as constants
TAX_BRACKETS = {
    0: [(8350, 0.10), (33950, 0.15), (82250, 0.25), (171550, 0.28), (372950, 0.33), (float('inf'), 0.35)],
    1: [(16700, 0.10), (67900, 0.15), (137050, 0.25), (208850, 0.28), (372950, 0.33), (float('inf'), 0.35)],
    2: [(8350, 0.10), (33950, 0.15), (68525, 0.25), (104425, 0.28), (186475, 0.33), (float('inf'), 0.35)],
    3: [(11950, 0.10), (45500, 0.15), (117450, 0.25), (190200, 0.28), (372950, 0.33), (float('inf'), 0.35)]
}

def calculate_tax(income: float, status: int) -> float:
    """
    Calculates income tax based on filing status and taxable income.

    Args:
        income (float): Taxable income
        status (int): Filing status (0: Single, 1: Married Filing Jointly or Qualifying Widow(er), 2: Married Filing Separately, 3: Head of Household)

    Returns:
        float: Total tax
    """
    tax = 0
    prev_bracket = 0
    for bracket, rate in TAX_BRACKETS[status]:
        if income > bracket:
            tax += (bracket - prev_bracket) * rate
        else:
            tax += (income - prev_bracket) * rate
            break
        prev_bracket = bracket
    return tax

def main():
    print("Enter filing status:")
    print("0: Single")
    print("1: Married Filing Jointly or Qualifying Widow(er)")
    print("2: Married Filing Separately")
    print("3: Head of Household")
    
    while True:
        try:
            status = int(input("Enter filing status (0/1/2/3): "))
            if status not in TAX_BRACKETS:
                print("Invalid filing status. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    while True:
        try:
            income = float(input("Enter taxable income: "))
            if income < 0:
                print("Invalid income. Please enter a non-negative number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    tax = calculate_tax(income, status)
    print(f"Total tax: ${tax:.2f}")

if __name__ == "__main__":
    main()

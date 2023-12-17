# ui.landing_page.py

def main():
    categories = get_categories()
    display_menu(categories)
    calculator_name = get_user_selection(categories) # This will connect user input to calculator, can add print to see output
    return_user_selection(calculator_name)
    return calculator_name

def get_categories():
    # List of categories and calculators
    categories = {
    "Drug Administration": [
        "Drip and Flow rate",
        "Steroid Conversion"
    ],
    "Nephrology": [
        "CrCl - Cockcroft-Gault",
        "eGFR - CKD-EPI",
        "eGFR - MDRD"
    ],
    "Cardiology": [
        "QTc - Bazett",
        "QTc - Friderica",
        "QTc - Framingham",
        "QTc - Hodges",
        "ACSVD Risk Score"
    ],
    "Hematology and Oncology": [
        "R-IPSS",
        "WPSS",
    ],
    "Other": [
        "Half-Life",
        "Corrected Calcium",
        "Anion Gap",
        "Body Mass Index",
        "Ideal Body Weight"
    ]
    }

    return categories

def display_menu(categories):
    # Display list of categories
    RED = "\033[31m"
    BLUE = "\033[34m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    for cat_index, (category, calculators) in enumerate(categories.items(), start=1): # Enumerate is used to return index and key-pair value while .items() used to get key-pair values
        print(f"\n{BOLD}{BLUE}{cat_index}. {category}{RESET}")
        for calc_index, calculator in enumerate(calculators, start=1):
            print(f"{RED}[{cat_index}.{calc_index}] - {calculator}{RESET}")

    print()

def get_user_selection(categories):
    while True:
        try:
            user_selection = input("Enter your choice using a specific index ID from above (e.g. '1.1' would select 'Drip and Flow rate'): ").strip()

            # Splits the user selection into category index and item index (int conversion ensures it's an integer)
            cat_index, item_index = map(int, user_selection.split('.'))

            # Convert to 0-based index for list access
            cat_index -= 1
            item_index -= 1

            # Find and return the selected calculator
            try:
                category_keys = list(categories.keys())
                selected_category = category_keys[cat_index]
                return categories[selected_category][item_index]
            except IndexError:
                # Handles the case where the input is out of range
                print("Selection out of range. Please select a valid index.")
                continue

        except ValueError:
            # Handles the case where the input is not in the expected format
            print("Previously entered input is invalid")
            continue

def return_user_selection(calculator_name):
    # Return user input in terminal
    BOLD = "\033[1m"
    RESET = "\033[0m"
    print(f"\nYou selected the {BOLD}{calculator_name}{RESET} calculator. Please enter the required inputs below\n")

if __name__ == "__main__":
    main()

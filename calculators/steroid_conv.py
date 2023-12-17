# calculators.steroid_conv.py
import csv
import os
"""
Equation to calculate steroid conversion

:param med_from: Name of medication being converted FROM (to be selected from provided list by user)
:param med_from_value: Conversation value for medication being converted FROM (provided based on user selection)
:param dose_from: Dose of medication being converted FROM in mg (to be provided by user)
:param med_to: Name of medication being converted TO (to be selected from provided list by user)
:param med_to_value: Conversation value for medication being converted TO (provided based on user selection)

"""
def main():
    file_path = get_file_path()
    conversion_dict = get_conversion(file_path)
    display_conversion(conversion_dict)
    user_input = get_user_input(conversion_dict)
    result = calc_user_input(*user_input)
    print_result(*user_input, result)

def get_file_path():
    # Get file path for steroid conversion value, can't use direct file path since "steroid_conv.py" will be called in "main.py"
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'steroid_conv_value.csv')
    return file_path

def get_conversion(file_path):
    #Read in conversion values
    conversion_dict = {}

    with open(file_path, mode = "r") as file:
        csv_reader = csv.DictReader(file) # Note that "DictReader" automatically skips the first row compared to "Reader"
        for row in csv_reader:
            conversion_dict[row["Compound"]] = float(row["Conversion"])

    return conversion_dict

def display_conversion(conversion_dict):
    # Display list of categories
    RED = "\033[31m"
    BLUE = "\033[34m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    print(f"{BLUE}{BOLD}List of steroids{RESET}")

    for drug_index, drug in enumerate(conversion_dict.keys(), start=1):
        print(f"{RED}{drug_index}. {drug}{RESET}")

    print() # Add extra line

def get_user_input(conversion_dict):

    # Create list to use for medications and conversion factor (this is needed since a number is being used to call the dictionary content)
    dict_list = list(conversion_dict.items())

    # Retrieve medication converted FROM
    while True:
        try:
            med_from_selection = int(input("Enter the corresponding number (e.g. 1) of the medication converting 'FROM': ").strip())
            med_from_selection -= 1 # Convert to 0-based index for list access
            med_from = dict_list[med_from_selection][0] # Retrieve medication name
            med_from_value = dict_list[med_from_selection][1] # Retrieve medication conversion value
            break
        except IndexError:
            # Handles the case where the input is out of range
            print("Selection out of range. Please select a valid index.")
            continue
        except ValueError:
            # Handles the case where the input is not in the expected format
            print("Previously entered input is invalid")
            continue

    while True:
        try:
            dose_from = float(input("Enter medication dose (i.e. medication converting FROM) in mg: ").strip())
            break
        except ValueError:
            # Handles the case where the input is not in the expected format
            print("Previously entered input is invalid")
            continue

    while True:
        try:
            med_to_selection = int(input("Enter the corresponding number (e.g. 1) of the medication converting 'TO': ").strip())
            med_to_selection -= 1 # Convert to 0-based index for list access
            med_to = dict_list[med_to_selection][0] # Retrieve medication name
            med_to_value = dict_list[med_to_selection][1] # Retrieve medication conversion value
            break
        except IndexError:
            # Handles the case where the input is out of range
            print("Selection out of range. Please select a valid index.")
            continue
        except ValueError:
            # Handles the case where the input is not in the expected format
            print("Previously entered input is invalid")
            continue

    return med_from, med_from_value, med_to, med_to_value, dose_from

def calc_user_input(med_from, med_from_value, med_to, med_to_value, dose_from):
    # med_from and med_to are unused in order to avoid unpacking in main()
    result = (dose_from / med_from_value) * (med_to_value)
    return round(result, 1)

def print_result(med_from, med_from_value, med_to, med_to_value, dose_from, result):

    # Terminal color escape codes
    RED = "\033[31m"
    BLUE = "\033[34m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    def color_text(text, color):
        return f"{color}{text}{RESET}" # RESET is needed to revert terminal to default state

    # Print the summary with color in the terminal
    print(color_text("\nSummary of calculation", BOLD))
    print(color_text(f"Medication converting FROM = {med_from} (Conversion factor: {med_from_value})", RED))
    print(color_text(f"Medication converting TO = {med_to} (Conversion factor: {med_to_value})", RED))
    print(color_text(f"Dose of {med_from} = {dose_from} mg", RED))
    print(color_text(f"*** {dose_from} mg of {med_from} is equivalent to {result} mg of {med_to} \n", BLUE))

if __name__ == "__main__":
    main()

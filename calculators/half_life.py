# calculators.half_life.py

"""
Equation to calculate amount of medication remaining (in mg and %) based on half-life

:param quant_initial: Initial quantity (mg)
:param half_life: Half-life (hours)
:param time: Time period (hours)

"""

def main():
    user_input = get_user_input()
    result = calc_user_input(*user_input)
    print_result(*user_input, result)

def get_user_input(): # Can optionally add exceptions to handle ranges below
    while True:
        try:
            quant_initial = int(input("Enter intial quantity of medication (mg) = ").strip())
            break
        except ValueError:
            print("Invalid entry. Please enter a valid input")

    while True:
        try:
            half_life = float(input("Enter half-life (hours) = ").strip())
            break
        except ValueError:
            print("Invalid entry. Please enter a valid input")

    while True:
        try:
            time = float(input("Enter time period (hours) = ").strip())
            break
        except ValueError:
            print("Invalid entry. Please enter a valid input")

    return quant_initial, half_life, time

def calc_user_input(quant_initial, half_life, time):
    quant_remain = quant_initial * 0.5 ** (half_life / time)
    return round(quant_remain)

def print_result(quant_initial, time, half_life, result):
    RED = "\033[31m"
    BLUE = "\033[34m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    def color_text(text, color):
        return f"{color}{text}{RESET}"

    print(color_text("\nSummary of calculation", BOLD))
    print(color_text(f"Initial quantity of medication = {quant_initial} mg", RED))
    print(color_text(f"Half-life of medication = {half_life} ", RED))
    print(color_text(f"Time interval = {time} hours", RED))
    print(color_text(f"*** Amount of medication remaining = {result} mg ({result/quant_initial * 100}%) ***\n", BLUE))

if __name__ == "__main__":
    main()

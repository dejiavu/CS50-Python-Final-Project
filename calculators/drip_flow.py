# calculators.drip_flow.py

"""
Equation to calculate the drip rate for IV administration

:param volume_ml: The total volume in milliliters (mL)
:param drop_factor_gtt_ml: The number of drops in the delivery of 1 mL of solution (gtt/mL)
:param time_mins: Total duration of infusion in minutes (mins)

"""
def main():
    user_input = get_user_input()
    result = calc_user_input(*user_input)
    print_result(*user_input, result)

def get_user_input(): # Can optionally add exceptions to handle ranges below
    while True:
        try:
            volume_ml = float(input("Enter the volume to be given (mL) = ").strip())
            break
        except ValueError:
            print("Invalid volume. Please enter a valid input")

    while True:
        try:
            drop_factor_gtt_ml = float(input("Enter the drop factor (gtt/mL) = ").strip())
            break
        except ValueError:
            print("Invalid drop factor. Please enter a valid input")

    while True:
        try:
            time_mins = float(input("Enter the planned duration of the infusion (mins) = ").strip())
            break
        except ValueError:
            print("Invalid time. Please enter a valid input")

    return volume_ml, drop_factor_gtt_ml, time_mins

def calc_user_input(volume_ml, drop_factor_gtt_ml, time_mins):
    result = (volume_ml * drop_factor_gtt_ml) / (time_mins)
    return round(result)

def print_result(volume_ml, drop_factor_gtt_ml, time_mins, result):

    # Terminal color escape codes
    RED = "\033[31m"
    BLUE = "\033[34m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    def color_text(text, color):
        return f"{color}{text}{RESET}" # RESET is needed to revert terminal to default state

    # Print the summary with color in the terminal
    print(color_text("\nSummary of calculation", BOLD))
    print(color_text(f"Volume = {volume_ml} mL", RED))
    print(color_text(f"Drop factor = {drop_factor_gtt_ml} gtt/mL", RED))
    print(color_text(f"Time = {time_mins} min", RED))
    print(color_text(f"*** Drip rate = {result} gtt/min ***\n", BLUE))

if __name__ == "__main__":
    main()
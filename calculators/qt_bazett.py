# calculators.qt_bazett.py

"""
Equation to calculate corrected QT (QTc) interval based on Bazett formula

:param heart_rate: Heart rate (beats/min)
:param qt_interval: QT interval (msec)

"""

def main():
    user_input = get_user_input()
    result = calc_user_input(*user_input)
    print_result(*user_input, result)

def get_user_input(): # Can optionally add exceptions to handle ranges below
    while True:
        try:
            heart_rate = int(input("Enter Heart Rate (beats/min) = ").strip())
            break
        except ValueError:
            print("Invalid Heart Rate. Please enter a valid input")

    while True:
        try:
            qt_interval = float(input("Enter QT Interval (msec) = ").strip())
            break
        except ValueError:
            print("Invalid QT Interval. Please enter a valid input")

    return heart_rate, qt_interval

def calc_user_input(heart_rate, qt_interval):
    rr_interval = 60 / heart_rate
    result = qt_interval / rr_interval ** (1/2)
    return round(result)

def print_result(heart_rate, qt_interval, result):
    RED = "\033[31m"
    BLUE = "\033[34m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    def color_text(text, color):
        return f"{color}{text}{RESET}"

    print(color_text("\nSummary of calculation", BOLD))
    print(color_text(f"Heart Rate = {heart_rate} min/sec", RED))
    print(color_text(f"QT Interval = {qt_interval} msec", RED))
    print(color_text(f"*** QTc = {result} msec based on Bazett formula ***\n", BLUE))

if __name__ == "__main__":
    main()

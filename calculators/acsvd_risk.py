# calculators.acsvd_risk.py
# Reference: https://www.framinghamheartstudy.org/fhs-risk-functions/cardiovascular-disease-10-year-risk/
import csv
import os
import math
"""
Equation to obtain Cardiovascular Disease (10-year risk) - 2018 ACSVD 10-year Risk Calculator

:param sex: Sex (M/F)
:param age: Age (years)
:param total_chol: Total cholesterol (mg/dL)
:param hdl_chol: HDL cholesterol (mg/dL)
:param sbp_: Systolic blood pressure  (mmHg)
:param sbp_treated: Blood pressure treatment (Yes/No)
:param smoke_yes: Smoking status (Yes/No)
:param diab_yes: Diabetes status (Yes/No)

"""
def main():
    file_path = get_file_path()
    print(file_path)
    coeff_dict = get_coefficients(file_path)
    user_input = get_user_input()
    result = calc_user_input(*coeff_dict, *user_input)
    print_result(*user_input, result)

def get_file_path():
    # Get file path for steroid conversion value, can't use direct file path since "framingham_risk_value.csv" will be called in "main.py"
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'acsvd_risk_value.csv')
    return file_path

def get_coefficients(file_path):
    #Read in conversion values

    # Coefficients for male and female
    coeff_male = {}
    coeff_female = {}

    with open(file_path, mode = "r") as file:
        csv_reader = csv.DictReader(file) # Note that "DictReader" automatically skips the first row compared to "Reader"
        for row in csv_reader:
            coeff_male[row["Variable"]] = float(row["Beta_male"])

    with open(file_path, mode = "r") as file:
        csv_reader = csv.DictReader(file) # Note that "DictReader" automatically skips the first row compared to "Reader"
        for row in csv_reader:
            coeff_female[row["Variable"]] = float(row["Beta_female"])

    return coeff_male, coeff_female

def get_user_input(): # Can optionally add exceptions to handle ranges
    while True:
        try:
            sex = (input("Enter sex ('M' for male and 'F' for female) = ").strip().upper())
            if sex not in ["M", "F"]:
                print("Sex is incorrectly inputed, enter 'M' for male and 'F' for female")
                continue
            break
        except ValueError:
            print("Invalid sex. Please enter a valid input")

    while True:
        try:
            age = int(input("Enter age (yrs) = ").strip())
            break
        except ValueError:
            print("Invalid age. Please enter a valid input")

    while True:
        try:
            total_chol = float(input("Enter Total Cholesterol (mg/dL) = ").strip())
            break
        except ValueError:
            print("Invalid Total Cholesterol. Please enter a valid input")

    while True:
        try:
            hdl_chol = float(input("Enter HDL Cholesterol (mg/dL) = ").strip())
            break
        except ValueError:
            print("Invalid HDL Cholesterol. Please enter a valid input")

    while True:
        try:
            sbp = int(input("Enter Systolic Blood Pressure (mmHg) = ").strip())
            break
        except ValueError:
            print("Invalid Systolic Blood Pressure. Please enter a valid input")

    while True:
        try:
            sbp_treated = (input("If on treatment for high blood pressure, enter Y, otherwise, enter N = ").strip().upper())
            if sbp_treated not in ["Y", "N"]:
                print("Blood pressure treatment status is incorrectly inputed. If on treatment for high blood pressure, enter 'Y', otherwise, enter 'N'")
                continue
            break
        except ValueError:
            print("Invalid entry. Please enter a valid input")

    while True:
        try:
            smoke_yes = (input("If currently smoking, enter Y, otherwise, enter N = ").strip().upper())
            if smoke_yes not in ["Y", "N"]:
                print("Smoking status is incorrectly inputed. If currently smoking, enter 'Y', otherwise, enter 'N'")
                continue
            break
        except ValueError:
            print("Invalid entry. Please enter a valid input")

    while True:
        try:
            diab_yes = (input("If currently diagnosed for diabetes, enter Y, otherwise, enter N = ").strip().upper())
            if diab_yes not in ["Y", "N"]:
                print("Diabetes status is incorrectly inputed. If currently diagnosed for diabetes, enter 'Y', otherwise, enter 'N'")
                continue
            break
        except ValueError:
            print("Invalid entry. Please enter a valid input")

    return sex, age, total_chol, hdl_chol, sbp, sbp_treated, smoke_yes, diab_yes

def calc_user_input(coeff_male, coeff_female, sex, age, total_chol, hdl_chol, sbp, sbp_treated, smoke_yes, diab_yes):
    if sex == "M":
        coeff = coeff_male
        base_risk, offset = 0.88936, 23.9802 # Regression values for male
    else:
        coeff = coeff_female
        base_risk, offset = 0.95012, 26.1931 # Regression values for female

    age_value = math.log(age) * coeff["Age_log"]
    total_chol_value = math.log(total_chol) * coeff["Total_chol_log"]
    hdl_chol_value = math.log(hdl_chol) * coeff["HDL_chol_log"]
    sbp_value = math.log(sbp) * coeff["SBP_treated_log"] if sbp_treated == "Y"  else math.log(sbp) * coeff["SBP_untreated_log"]
    smoke_value = coeff["Smoking_yes"] if smoke_yes == "Y"  else 0
    diab_value = coeff["Diabetes_yes"] if diab_yes == "Y"  else 0
    total_value = age_value + total_chol_value + hdl_chol_value + sbp_value + smoke_value + diab_value
    risk = 1 - math.pow(base_risk, math.exp(total_value - offset))
    risk = round(risk * 100, 2)

    return risk

def print_result(sex, age, total_chol, hdl_chol, sbp, sbp_treated, smoke_yes, diab_yes, result):
    RED = "\033[31m"
    BLUE = "\033[34m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    def color_text(text, color):
        return f"{color}{text}{RESET}"

    print(color_text("\nSummary of calculation", BOLD))
    print(color_text(f"Sex = {sex}", RED))
    print(color_text(f"Age = {age} years", RED))
    print(color_text(f"Total Cholesterol = {total_chol} mg/dL", RED))
    print(color_text(f"HDL Cholesterol = {hdl_chol} mg/dL", RED))
    print(color_text(f"Systolic Blood Pressure = {sbp} mmHg", RED))
    print(color_text(f"Blood Pressure Treatment = {sbp_treated}", RED))
    print(color_text(f"Smoking Status = {smoke_yes}", RED))
    print(color_text(f"Diabetes Status = {diab_yes}", RED))
    print(color_text(f"*** 10 Year Risk of Cardiovascular Disease = {result}% ***\n", BLUE))


if __name__ == "__main__":
    main()

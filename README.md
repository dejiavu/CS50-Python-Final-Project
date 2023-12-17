# Medical Calculator Suite

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Usage](#usage)
- [Acknowledgments](#acknowledgments)

## Overview
The Medical Calculator Suite is a collection of various medical calculators designed to help with common medical equations. The calculator takes user input and provide results via a command line interface. The current suite includes **17 calculators** grouped into 4 categories (**Drug Administration, Nephrology, Cardiology, Hematology/Oncology, and Others**). Future plans to optimize the suite include:
* Including generation of PDF output of results
* Expansion of suite of calculators
* Interactive web interface (in place of terminal)

## Requirements
There are no pip-installable libraries or requirments.

## Usage
### Directions
**Step 1**: Open a terminal or command prompt, navigate to the project directory, and run the application using Python. To start the application, run:

```bash
python project.py
```
**Step 2**: Select a calculator from the list displayed by using the corresponding index (e.g. 1.1, 1.2, 1.3) shown. For example, entering **1.1** would select the **Drip and Flow rate** caclulator.

**Step 3**: Enter values for requested variable. Once completed, entered values and results will be displated in terminal.

Exit the calculator at anytime via `KeyboardInterrupt` (i.e. control + C on Mac).

##Enter YouTube walkthrough link###

### List of Calculators
| Category                 | Calculators                                         |
|--------------------------|-----------------------------------------------------|
| **Drug Administration**      | Drip and Flow rate<br>Steroid Conversion            |
| **Nephrology**               | Cockcroft-Gault Formula<br>CKD-EPI 2021<br>MDRD eGFR                 |
| **Cardiology**               | Corrected QT Bazett<br>Corrected QT Friderica<br>Corrected QT Framingham<br>Corrected QT Hodges<br>ACSVD Risk Score |
| **Hematology and Oncology**  | R-IPSS<br>WPSS                                      |
| **Other**                    | Half-Life<br>Corrected Calcium<br>Anion Gap<br>Body Mass Index<br>Ideal Body Weight |

### Explanation of Calculators
***(Listed in alphabetical order of file name in [calculators](/project/calculators) folder)***

**ACSVD Risk Score**: Calculates the 2018 ACSVD 10-year Risk score and is contained in `acsvd_risk.py`. This calculator uses regression values which are contained in `acsvd_risk_value.csv`. Input parameters are - ***sex (M/F)***, ***age (years)***, ***total cholesterol (mg/dL)***, ***HDL cholesterol (mg/dL)***, ***systolic blood pressure (mmHg)***, ***blood pressure treatment (Yes/No)***, ***smoking status (Yes/No)***, and ***diabetes status (Yes/No)***.

**Anion Gap**: Calculates anion gap and is contained in `anion_gap.py`. Input parameters are - ***sodium (mEq/L)***, ***chloride (mEq)***, and ***bicarbonate (mEq/L)***.

**Corrected Calcium**: Calculates corrected calcium and is contained in `corr_calcium.py`. Input parameters are ***calcium (mg/dL)***, ***patient's albumin (g/dL)***, ***normal albumun value (g/dL)***.

**Cockcroft-Gault Formula**: Calculates creatinine clearance based on Cockcroft-Gault equation and is contained in `crcl_cg.py`. Input parameters are ***age (yrs)***, ***weight (kg)***, ***serum creatinine concetration (mg/dL)***, and ***sex (M/F)***.

**Drip and Flow rate**: Calculates the drip rate for IV administration and is contained in `drip_flow.py`. Input parameters are total ***volume in milliliters (mL)***, the ***number of drops (gtt/mL)*** in the delivery of 1 mL of solution total, and ***duration of infusion (mins)***.

**CKD-EPI 2021**: Calculates estimated GFR based on CKD-EPI 2021 and is contained in `egfr_ckd_2021.py`. Input parameters are
***age (yrs)***,
***serum creatinine concetration (mg/dL)***,
***sex (M/F)***

**MDRD eGFR**: Calculates estimated GFR based on CKD-EPI 2021 and is contained in `egfr_mdrd.py`. Input parameters are
***age (yrs)***, ***serum creatinine concetration (mg/dL)***, ***sex (M/F)***, annd ***black race (Y/N)***.

**Half-Life**: Calculates amount of medication remaining (in mg and %) based on half-life and is contained in `half_life.py`. Input parameters are
***initial quantity (mg)*** of medication, ***half-life (hours)*** of medication, and ***time period (hours)***.

**Corrected QT Bazett**: Calculates corrected QT (QTc) interval based on Bazett formula and is contained in `qt_bazett.py`. Input parameters are ***heart rate (beats/min)*** and ***QT interval (msec)***

**Corrected QT Framingham**: Calculates corrected QT (QTc) interval based on Framingham formula and is contained in `qt_framingham.py`. Input parameters are ***heart rate (beats/min)*** and ***QT interval (msec)***

**Corrected QT Friderica**: Calculates corrected QT (QTc) interval based on Friderica formula and is contained in `qt_friderica.py`. Input parameters are ***heart rate (beats/min)*** and ***QT interval (msec)***

**Corrected QT Hodges**: Calculates corrected QT (QTc) interval based on Hodges formula and is contained in `qt_hodges.py`. Input parameters are
***Heart rate (beats/min)*** and ***QT interval (msec)***

**R-IPSS**: Calculates R-IPSS (revised International Prostate Symptom Score) risk score and is contained in  `r_ipss.py`. Input parameters are ***hemoglobin (g/dL)***, ***absolute neutrophil count (ANC) (x10^9/L)***, ***platelet (x10^9/L)***, ***bone marrow blast (%)***, and ***cytogenetics***.

**Steroid Conversion**: Calculates steroid dose based on conversion factors and is contained in `steroid_conv.py`. This calculator uses conversion factors which are contained in `steroid_conv_value.csv`. Input parameters are ***name*** and ***dose*** of medications.

**Body Mass Index**: Calculates Body Mass Index (BMI) and is contained in `weight_bmi.py`. Input parameters are ***weight (lbs)*** and ***height (inches)***

**Ideal Body Weight**: Calculates Ideal Body Weight (IBW) and is contained in `weight_ibw.py`. Input parameters are ***sex (M/F)*** and ***height (inches)***

**WPSS**: Calculates WPSS (WHO prognostic scoring system) risk score and is contained in `wpss.py` . Input parameters are ***WHO category***, ***karyotype*** and ***tranfusion status (Y/N)***

### Testing calculators
All functions have corresponding test functions. To evaluate all test function, run:

```bash
pytest test_project.py
```
To review and evaluate individual test function go to [project/tests](/project/tests). All test have the same name as the calculator functions, prepended with `test`. For example, (`test_anion_gap`) is the test function for the `anion_gap.py`.

## Acknowledgments
The following sites were utilized in the generation of the calculators
* https://www.mdcalc.com
* https://www.framinghamheartstudy.org

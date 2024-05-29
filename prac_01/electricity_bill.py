"""
display title Electricity Bill
get cents per kWh
get daily use in kWh
get number of billing days
print estimated bill string with output
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print(f"Electricity bill estimator")
tariff_input = int(input("Which tariff? 11 or 31 "))
if tariff_input == 11:
    daily_use = float(input("Enter daily use in kWh: "))
    billing_days = int(input("Enter number of billing days: "))
    print(f"Estimated bill: ", "$", TARIFF_11 * daily_use * billing_days)
elif tariff_input == 31:
    daily_use = float(input("Enter daily use in kWh: "))
    billing_days = int(input("Enter number of billing days: "))
    print(f"Estimated bill: ", "$", TARIFF_31 * daily_use)
else:
    print("Invalid input")

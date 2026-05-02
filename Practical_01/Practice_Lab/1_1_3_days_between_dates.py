# 1.1.3. Days Between Two Dates

from datetime import date

def calculate_days(first_date_str, second_date_str):
    d1 = date.fromisoformat(first_date_str)
    d2 = date.fromisoformat(second_date_str)
    delta = d2 - d1
    return delta

date1_str = input().strip()
date2_str = input().strip()

print(abs(calculate_days(date1_str, date2_str).days))

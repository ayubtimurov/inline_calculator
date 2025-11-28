import re

def safe_calculate(expression: str):
    expression = expression.replace(" ", "")
    # The original regex from main.py
    if not re.match(r"^[\d+\-\*\/\(\)\.]$", expression):
        raise ValueError("Invalid charachters")
    return eval(expression)

try:
    print(f"Calculating '5+4': {safe_calculate('5+4')}")
except ValueError as e:
    print(f"Error calculating '5+4': {e}")

try:
    print(f"Calculating '5': {safe_calculate('5')}")
except ValueError as e:
    print(f"Error calculating '5': {e}")

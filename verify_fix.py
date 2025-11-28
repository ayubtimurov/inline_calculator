import re

# Copy of the fixed function from main.py
def safe_calculate(expression: str):
    expression = expression.replace(" ", "")

    if not re.match(r"^[\d+\-\*\/\(\)\.]+$", expression):
        raise ValueError("Invalid charachters")
    return eval(expression)

try:
    result = safe_calculate('5+4')
    print(f"Calculating '5+4': {result}")
    assert result == 9
    print("Test '5+4' PASSED")
except Exception as e:
    print(f"Test '5+4' FAILED: {e}")

try:
    result = safe_calculate('10*2')
    print(f"Calculating '10*2': {result}")
    assert result == 20
    print("Test '10*2' PASSED")
except Exception as e:
    print(f"Test '10*2' FAILED: {e}")

try:
    safe_calculate('5+a')
    print("Test '5+a' FAILED (should have raised ValueError)")
except ValueError:
    print("Test '5+a' PASSED (raised ValueError as expected)")
except Exception as e:
    print(f"Test '5+a' FAILED (raised wrong exception: {e})")

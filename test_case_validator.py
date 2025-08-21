def is_valid(case: str) -> bool:
    """
    Returns True if the test case is valid:
    - Starts with 'TC_'
    - Followed by exactly 3 digits
    """
    if not case.startswith("TC_"):
        return False
    if len(case) != 6:
        return False
    digits = case[3:]
    return digits.isdigit()

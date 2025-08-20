# Takes a list of test case IDs and verifies naming format (e.g., "TC_001")
test_cases = ["TC_001", "001_TC", "TC_002", "TC3"]
# Output: Which ones are valid

for case in test_cases:
    if case.startswith("TC_") and len(case) == 6 and case[3:].isdigit():
        print(case)
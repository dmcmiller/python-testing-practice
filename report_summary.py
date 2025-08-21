# Given a list of test results (pass/fail), calculate pass rate and generate a short summary
# Input: ["pass", "fail", "pass", "pass"]
# Output: "Total: 4 | Passed: 3 | Pass Rate: 75%"

results = ["pass", "fail", "pass", "pass", "fail"]

def summary(test_results):
    total_number = 0
    total_pass = 0
    total_fail = 0
    for grade in results:
        total_number +=1
        if grade == 'pass':
            total_pass += 1
        else:
            total_fail += 1
    pass_rate = (total_pass / total_number) * 100

    print(f"Total: {total_number} | Passed: {total_pass} | Pass Rate: {pass_rate} ")
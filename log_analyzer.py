# Simulate reading a test log file and extract lines containing "ERROR"
# Use file reading and basic string operations

read_log = open("sample_log.txt")
for line in read_log:
    if "ERROR" in line:
        print(line)

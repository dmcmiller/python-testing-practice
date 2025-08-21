# Simulate reading a test log file and extract lines containing "ERROR"
# Use file reading and basic string operations

def extract_errors(file):
    read_log = open(file)
    for line in read_log:
        if "ERROR" in line:
            print(line)

extract_errors("sample_log.txt")
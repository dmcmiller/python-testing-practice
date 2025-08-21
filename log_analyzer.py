def extract_errors(file_path: str) -> list:
    """
    Reads a text file and returns a list of lines containing 'ERROR'
    """
    try:
        with open(file_path, 'r') as f:
            return [line.strip() for line in f if "ERROR" in line]
    except FileNotFoundError:
        return []

import tempfile
import os
from log_analyzer import extract_errors

def test_extract_errors_finds_error():
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
        tmp.write("INFO - all good\nERROR - something broke\n")
        tmp.flush()
        path = tmp.name

    errors = extract_errors(path)
    os.remove(path)
    assert "ERROR - something broke" in errors

def test_extract_errors_no_error():
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
        tmp.write("INFO - okay\n")
        tmp.flush()
        path = tmp.name

    errors = extract_errors(path)
    os.remove(path)
    assert errors == []

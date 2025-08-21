from log_analyzer import extract_errors
import tempfile
import os

def test_extract_errors_finds_error():
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
        tmp.write("INFO - all good\n")
        tmp.write("ERROR - something broke\n")
        tmp_path = tmp.name
    
    errors = extract_errors(tmp_path)
    os.remove(tmp_path)
    assert "ERROR - something broke" in errors

def test_extract_errors_empty_file():
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
        tmp_path = tmp.name
    
    errors = extract_errors(tmp_path)
    os.remove(tmp_path)
    assert errors == []

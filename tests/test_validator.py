from test_case_validator import is_valid

def test_valid_case():
    assert is_valid("TC_001")

def test_invalid_case():
    assert not is_valid("001_TC")

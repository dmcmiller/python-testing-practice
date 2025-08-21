def summarize_results(results: list) -> dict:
    """
    Returns a summary dictionary:
    - total: total number of results
    - passed: number of 'pass' results
    - rate: pass percentage
    """
    total = len(results)
    passed = results.count("pass")
    rate = (passed / total) * 100 if total > 0 else 0
    return {"total": total, "passed": passed, "rate": rate}

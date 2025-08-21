from report_summary import summarize_results

def test_summary_normal():
    results = ["pass", "fail", "pass"]
    summary = summarize_results(results)
    assert summary["total"] == 3
    assert summary["passed"] == 2
    assert round(summary["rate"], 2) == round((2/3)*100, 2)

def test_summary_empty():
    summary = summarize_results([])
    assert summary["total"] == 0
    assert summary["passed"] == 0
    assert summary["rate"] == 0

"""Turn pytest's results.xml into a score table.

Used by the GitHub Actions workflow, but you can run it yourself too:
    pytest --junitxml=results.xml
    python tools/score.py results.xml
"""

import os
import sys
import xml.etree.ElementTree as ET

LABELS = {
    "test_a1_celsius_to_fahrenheit": "A1 celsius_to_fahrenheit",
    "test_a2_is_even": "A2 is_even",
    "test_a3_get_grade": "A3 get_grade",
    "test_a4_ticket_price": "A4 ticket_price",
    "test_a5_format_greeting": "A5 format_greeting",
    "test_b1_sum_of_evens": "B1 sum_of_evens",
    "test_b2_largest": "B2 largest",
    "test_b3_reverse_words": "B3 reverse_words",
    "test_b4_word_count": "B4 word_count",
    "test_b5_remove_duplicates": "B5 remove_duplicates",
    "test_c1_average": "C1 average",
    "test_c2_class_report": "C2 class_report",
    "test_c3_top_student": "C3 top_student",
    "test_c4_shopping_total": "C4 shopping_total",
    "test_c5_password_strength": "C5 password_strength",
}


def read_results(path):
    """Return {test_name: (passed, short_message)} for every known exercise."""
    results = {name: (False, "not run (file has an error?)") for name in LABELS}
    if not os.path.exists(path):
        return results
    root = ET.parse(path).getroot()
    for case in root.iter("testcase"):
        name = case.get("name")
        if name not in LABELS:
            continue
        problem = case.find("failure")
        if problem is None:
            problem = case.find("error")
        if problem is None:
            results[name] = (True, "")
        else:
            message = (problem.get("message") or "failed").splitlines()[0]
            results[name] = (False, message[:120])
    return results


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "results.xml"
    results = read_results(path)
    passed = sum(1 for ok, _ in results.values() if ok)
    total = len(results)

    lines = [
        f"## Score: {passed}/{total}",
        "",
        "| Exercise | Result | Hint |",
        "| --- | --- | --- |",
    ]
    for name, label in LABELS.items():
        ok, message = results[name]
        hint = message.replace("|", "\\|")
        lines.append(f"| {label} | {'✅ pass' if ok else '❌ fail'} | {hint} |")
    report = "\n".join(lines)

    print(report)
    print(f"\nSCORE: {passed}/{total}")

    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_file:
        with open(summary_file, "a", encoding="utf-8") as f:
            f.write(report + "\n")


if __name__ == "__main__":
    main()

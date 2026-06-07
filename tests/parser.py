import sys
import json
import re

def parse_pytest_output(output):
    """Parse pytest output into Silver-compatible format"""
    results = []
    
    # Match test lines like "test_delete_middle_task PASSED" or "FAILED"
    for line in output.splitlines():
        if any(test in line for test in ["test_", "PASSED", "FAILED", "SKIPPED"]):
            match = re.search(r'(test_\w+).*?(PASSED|FAILED|ERROR|SKIPPED)', line)
            if match:
                test_name = match.group(1)
                status = match.group(2).lower()
                results.append({"name": test_name, "status": status})
    
    return results

if __name__ == "__main__":
    output = sys.stdin.read()
    results = parse_pytest_output(output)
    print(json.dumps(results))

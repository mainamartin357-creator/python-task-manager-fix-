#!/bin/bash
set -e

# Apply test patch if provided (usually empty for this task)
if [ -n "$TEST_PATCH" ]; then
    echo "$TEST_PATCH" | git apply --index || true
fi

# Run the test script and capture output
chmod +x run_script.sh
./run_script.sh | python parser.py > /tmp/test_results.json

# Verify results using config
python -c '
import json, sys
with open("tests/config.json") as f:
    config = json.load(f)
with open("/tmp/test_results.json") as f:
    results = json.load(f)

result_dict = {r["name"]: r["status"] for r in results}

fail_to_pass = all(result_dict.get(t, "failed") == "passed" for t in config["fail_to_pass"])
pass_to_pass = all(result_dict.get(t, "failed") == "passed" for t in config["pass_to_pass"])

success = fail_to_pass and pass_to_pass
print("All required tests passed" if success else "Some tests failed")
with open("/logs/verifier/reward.txt", "w") as f:
    f.write("1" if success else "0")
'

echo "Test harness completed."

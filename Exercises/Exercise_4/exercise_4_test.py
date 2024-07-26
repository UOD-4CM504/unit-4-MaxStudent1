# test_exercise_4.py

import pytest
import subprocess
import sys
import os

def run_exercise_4(input_size):
    script_path = os.path.join(os.path.dirname(__file__), "exercise_4.py")
    process = subprocess.Popen(
        [sys.executable, script_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=str(input_size))
    return stdout.strip()

def normalize_output(output):
    # Split the output into lines, remove any empty lines, and strip each line
    return '\n'.join(line.strip() for line in output.split('\n') if line.strip())

@pytest.mark.parametrize("size, expected_output", [
    (3, "*\n**\n***"),
    (5, "*\n**\n***\n****\n*****"),
    (1, "*"),
    (6, "*\n**\n***\n****\n*****\n******"),
])
def test_exercise_4(size, expected_output):
    output = run_exercise_4(size)
    normalized_output = normalize_output(output)
    normalized_expected = normalize_output(expected_output)
    assert normalized_expected in normalized_output, f"For size {size}:\nExpected:\n{normalized_expected}\n\nGot:\n{normalized_output}"

if __name__ == "__main__":
    pytest.main([__file__])
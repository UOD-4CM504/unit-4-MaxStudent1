import pytest
import subprocess
import sys
import os


def run_exercise_4_3(inputs):
    script_path = os.path.join(os.path.dirname(__file__), "exercise_3.py")
    process = subprocess.Popen(
        [sys.executable, script_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input='\n'.join(map(str, inputs)))
    return stdout.strip()


def normalize_output(output):
    # Remove all whitespace and convert to lowercase
    return ''.join(output.lower().split())


@pytest.mark.parametrize("inputs, expected_output", [
    ([3, 10, 32, -1, 0], "The largest of the numbers entered is 32"),
    ([-5, -10, -3, -1, 0], "The largest of the numbers entered is -1"),
    ([0], "No numbers entered."),
    ([100, 50, 75, 0], "The largest of the numbers entered is 100"),
])
def test_exercise_4_3(inputs, expected_output):
    output = run_exercise_4_3(inputs)
    normalized_output = normalize_output(output)
    normalized_expected = normalize_output(expected_output)

    assert normalized_expected in normalized_output, f"For inputs {inputs}:\nExpected output containing: {expected_output}\nGot: {output}"


if __name__ == "__main__":
    pytest.main([__file__])
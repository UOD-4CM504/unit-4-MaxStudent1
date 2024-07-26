import pytest
import subprocess
import sys
import os


def run_exercise_1(inputs):
    script_path = os.path.join(os.path.dirname(__file__), "exercise_1.py")
    process = subprocess.Popen(
        [sys.executable, script_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input='\n'.join(inputs))
    return stdout.strip()


def get_final_output(output):
    lines = output.split('\n')
    return lines[-1] if lines else ""


@pytest.mark.parametrize("inputs, expected_output", [
    (["3", "6.1", "0"], "The average of the numbers entered is 4.55"),
    (["0"], "No numbers entered."),
    (["1", "2", "3", "0"], "The average of the numbers entered is 2.0"),
])
def test_exercise_1(inputs, expected_output):
    full_output = run_exercise_1(inputs)
    final_output = get_final_output(full_output)
    assert final_output == expected_output, f"Expected:\n{expected_output}\n\nGot:\n{final_output}"


if __name__ == "__main__":
    pytest.main([__file__])

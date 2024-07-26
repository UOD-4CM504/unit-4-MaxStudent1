import pytest
import subprocess
import sys
import os


def run_exercise_4_5(inputs):
    script_path = os.path.join(os.path.dirname(__file__), "exercise_5.py")
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


@pytest.mark.parametrize("inputs, expected_outputs", [
    ([2, 5, 3],
     ["Your guess is too low", "Your guess is too high", "Well done the correct answer was 3", "You took 3 guesses"]),
    ([0], ["Program exited", "The correct answer was 3"]),
    ([2, 0], ["Your guess is too low", "Program exited", "The correct answer was 3"]),
])
def test_exercise_4_5(inputs, expected_outputs):
    output = run_exercise_4_5(inputs)
    normalized_output = normalize_output(output)

    for expected in expected_outputs:
        normalized_expected = normalize_output(expected)
        assert normalized_expected in normalized_output, f"For inputs {inputs}:\nExpected output containing: {expected}\nGot: {output}"


if __name__ == "__main__":
    pytest.main([__file__])
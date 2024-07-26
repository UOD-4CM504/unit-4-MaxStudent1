# test_print_numbers.py

import pytest
import subprocess
import sys
import os


def test_print_numbers():
    # Get the path to the script
    script_path = os.path.join(os.path.dirname(__file__), "BreakAndContinue.py")

    # Run the script and capture its output
    result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)

    # Split the output into lines and convert to integers
    output_numbers = [int(num) for num in result.stdout.strip().split('\n')]

    # Check if the output has exactly 99 numbers (100 - 1 for the excluded 42)
    assert len(output_numbers) == 99, f"Expected 99 numbers, but got {len(output_numbers)}"

    # Check if the numbers are in the correct range and order
    expected_numbers = list(range(1, 42)) + list(range(43, 101))
    assert output_numbers == expected_numbers, "The output doesn't match the expected sequence"

    # Check if 42 is not in the output
    assert 42 not in output_numbers, "42 should not be in the output"

    # Check if the first number is 1 and the last number is 100
    assert output_numbers[0] == 1, f"The first number should be 1, but got {output_numbers[0]}"
    assert output_numbers[-1] == 100, f"The last number should be 100, but got {output_numbers[-1]}"

    print("All tests passed successfully!")


if __name__ == "__main__":
    pytest.main([__file__])
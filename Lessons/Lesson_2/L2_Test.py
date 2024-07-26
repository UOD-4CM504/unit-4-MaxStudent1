# test_odd_numbers.py

import pytest
import subprocess
import ast


def test_odd_numbers():
    # Run the script and capture its output
    result = subprocess.run(['python', 'L2_Exercise.py'], capture_output=True, text=True)

    # Check if there's any output
    assert result.stdout.strip(), "No output captured from the script"

    # Convert the string representation of the list to an actual list
    try:
        output_list = ast.literal_eval(result.stdout.strip())
    except:
        pytest.fail(f"Failed to parse output as a list. Output: {result.stdout.strip()}")

    # Check if it's a list
    assert isinstance(output_list, list), "Output is not a list"

    # Check if all numbers are odd
    assert all(num % 2 == 1 for num in output_list), "Not all numbers are odd"

    # Check if the numbers are in ascending order
    assert output_list == sorted(output_list), "Numbers are not in ascending order"

    # Check if the first number is 1 and the last number is 99
    assert output_list[0] == 1, f"The first number is not 1, it's {output_list[0]}"
    assert output_list[-1] == 99, f"The last number is not 99, it's {output_list[-1]}"

    # Check if all odd numbers between 1 and 99 are present
    expected_numbers = list(range(1, 100, 2))
    assert output_list == expected_numbers, "Not all odd numbers between 1 and 99 are present"

    # Check the total count of numbers
    assert len(output_list) == 50, f"Incorrect number of odd numbers. Expected 50, got {len(output_list)}"

    # Print the output for verification
    print(f"Script output: {result.stdout.strip()}")
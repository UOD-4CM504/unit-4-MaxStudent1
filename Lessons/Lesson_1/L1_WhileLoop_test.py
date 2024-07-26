# test_even_numbers.py

import pytest
import io
import sys
import subprocess

def test_even_numbers():
    # Run the script and capture its output
    result = subprocess.run(['python', 'L1_WhileLoop.py'], capture_output=True, text=True)
    output = result.stdout.strip().split('\n')

    # Convert the output to a list of integers
    output_numbers = [int(num) for num in output]

    # Check if all numbers are even
    assert all(num % 2 == 0 for num in output_numbers), "Not all numbers are even"

    # Check if the numbers are in ascending order
    assert output_numbers == sorted(output_numbers), "Numbers are not in ascending order"

    # Check if the first number is 2 and the last number is 100
    assert output_numbers[0] == 2, "The first number is not 2"
    assert output_numbers[-1] == 100, "The last number is not 100"

    # Check if all even numbers between 2 and 100 are present
    expected_numbers = list(range(2, 101, 2))
    assert output_numbers == expected_numbers, "Not all even numbers between 2 and 100 are present"

    # Check the total count of numbers
    assert len(output_numbers) == 50, "Incorrect number of even numbers"
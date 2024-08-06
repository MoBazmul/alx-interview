# Min Operations

## Description

This program calculates the minimum number of operations required to obtain exactly `n` 'H' characters in a file using only two operations: "Copy All" and "Paste".

The `minOperations` function works by factorizing the number `n` into its prime factors. Each prime factor represents the number of "Paste" operations needed after a "Copy All" operation. The total number of operations is the sum of these prime factors.

## Function

### `minOperations(n)`

- **Parameters:**
  - `n` (int): The target number of 'H' characters in the file.

- **Returns:**
  - `int`: The minimum number of operations required to reach exactly `n` 'H' characters. Returns 0 if `n` is less than or equal to 1.

## Usage

1. Save the `minOperations` function in a file named `0-minoperations.py`.
2. Create a test script in a file named `0-main.py` as shown below:

    ```python
    #!/usr/bin/python3
    """
    Main file for testing the minOperations function.
    """

    minOperations = __import__('0-minoperations').minOperations

    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
    ```

3. Make both files executable:

    ```bash
    chmod +x 0-minoperations.py
    chmod +x 0-main.py
    ```

4. Run the test script:

    ```bash
    ./0-main.py
    ```

## Examples

- For `n = 4`, the output will be `4` because it takes 4 operations to reach exactly 4 'H' characters.
- For `n = 12`, the output will be `7` because it takes 7 operations to reach exactly 12 'H' characters.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



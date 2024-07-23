# Pascal's Triangle

This repository contains a Python function that generates Pascal's Triangle up to a specified number of rows. Pascal's Triangle is a triangular array of the binomial coefficients, where each number is the sum of the two numbers directly above it.

## Function Description

### `pascal_triangle(n)`

The `pascal_triangle` function takes an integer `n` and returns a list of lists of integers representing Pascal’s Triangle with `n` rows.

- **Parameters:**
  - `n` (int): The number of rows in Pascal's Triangle.

- **Returns:**
  - `List[List[int]]`: A list of lists representing Pascal’s Triangle. Returns an empty list if `n` is less than or equal to 0.

### Usage

```python
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle

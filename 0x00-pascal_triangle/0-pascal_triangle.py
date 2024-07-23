#!/usr/bin/python3
"""
  This program creates the famous Pascal's triangle, which is a Triangular array of the Binomial coefficients
"""

def pascal_triangle(n):
    """
      This functions implements the pascals triangle
    """
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

if __name__ == "__main__":
    """
      Testing the function
    """
    def print_triangle(triangle):
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
# Lockboxes Problem

This program determines if all the boxes in a list of locked boxes can be opened. Each box may contain keys to other boxes, and the first box is always unlocked. Each key corresponds to the number of a box it can open.

## Description

The `canUnlockAll` function takes a list of lists as input, where each inner list contains the keys found in a corresponding box. It returns `True` if all boxes can be opened, otherwise `False`.

## Usage

1. Clone the repository or download the script.
2. Run the script with Python to test the function with the provided test cases.

## Function Prototype

```python
def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of lists): A list where each element is a list of keys contained in a box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """


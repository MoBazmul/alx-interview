#!/usr/bin/python3

"""
This program determines if all the boxes in a list of locked boxes can be opened.
Each box may contain keys to other boxes. The first box is always unlocked,
and each key corresponds to the number of a box it can open.

The `canUnlockAll` function takes a list of lists as input, where each inner list contains the keys
found in a corresponding box. It returns True if all boxes can be opened, otherwise False.

The main section of the program tests the function with various test cases.
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of lists): A list where each element is a list of keys contained in a box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = [0]  # Start with the first box opened
    
    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n and not opened[key]:
                opened[key] = True
                keys.append(key)
    
    return all(opened)

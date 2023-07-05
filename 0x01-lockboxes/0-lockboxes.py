#!/usr/bin/python3

"""
This module provides a method to determine if all boxes can be unlocked.
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True


    # Start with the keys from the first box
    keys = [0]

    while keys:
        box_idx = keys.pop()
        box = boxes[box_idx]

        for key in box:
            if key < num_boxes and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                keys.append(key)

    return all(unlocked_boxes)

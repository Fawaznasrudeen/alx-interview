#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened using depth-first searchh

    Args: 
    - boxes(list of lists): A list of lists representing the boxes and their keys.

    Returns: 
    -bool: True if all boxes can be opened, else False

    """

    visited = set()
    stack = [0]
    
    while stack:
        current_box = stack.pop()
        visited.add(current_box)

        for key in boxes[current_box]:
            if key not in visited:
                stack.append(key)
    return len(visited) == len(boxes)


#!/usr/bin/python3
"""
Lockboxes
"""


def __canUnlockAll(boxes, keys={0}, outrange={-1}):
    """
    Attributes:
        boxes(list of lists): all box
        keys(set): set of key
        outrange(set): set of key without box
    Return:
        True if all boxes can be opened, else return False
    """
    newkeys = {0}
    if sorted(range(len(boxes))) == sorted(keys - outrange):
        return True
    for i in keys - outrange:
        if i >= len(boxes):
            outrange.add(i)
        else:
            newkeys = set(boxes[i]) ^ newkeys
    if keys - outrange == newkeys | keys:
        return False
    return __canUnlockAll(boxes, (newkeys | keys), outrange)


def canUnlockAll(boxes):
    """
    Attributes:
        boxes: is a list of lists
    Return:
        True if all boxes can be opened, else return False
    """
    return __canUnlockAll(boxes)

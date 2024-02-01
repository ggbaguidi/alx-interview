#!/usr/bin/python3
"""
Write a method that determines if a given data set represents a
valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to
handle the 8 least significant bits of each integer
"""


def validUTF8(data):
    """UTF-8 Validation"""
    count = 0
    for byte in data:
        if(count == 0):
            if ((byte >> 7) == 0):
                continue

            if ((byte >> 5) == 0b110):
                count = 1
            elif ((byte >> 4) == 0b1110):
                count = 2
            elif ((byte >> 3) == 0b11110):
                count = 3
            else:
                return False
        else:
            if ((byte >> 6) != 0b10):
                return False
            count -= 1

    return (count == 0)

#!/usr/bin/python3

"""UTF-8 validation module."""


def validUTF8(data) -> bool:
    """Checks if the a list of integers are valid UTF-8 codepoints.

    @Params:
        data: The data to be tested.

    Returns: boolean value
    """

    def is_start_byte(byte) -> bool:
        """Helper function to check if the number is
        a valid start byte for UTF-8 character"""
        return (byte >> 6) == 2

    def is_continuation_byte(byte) -> bool:
        """Helper function to check if number given is a
        valid continuation"""
        return (byte >> 6) == 2

    remaining_bytes = 0

    for byte in data:
        byte = byte & 0xFF

        if remaining_bytes == 0:
            if (byte >> 7) == 0:
                continue
            elif (byte >> 5) == 6:
                remaining_bytes = 1
            elif (byte >> 4) == 14:
                remaining_bytes = 2
            elif (byte >> 3) == 30:
                remaining_bytes = 3
            else:
                return False
        else:
            if (byte >> 6) != 2:
                return False
            remaining_bytes -= 1

    if remaining_bytes > 0:
        return False

    return True

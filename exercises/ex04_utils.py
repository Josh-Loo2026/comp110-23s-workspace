"""EX04 - 'list' utility functions!"""

__author__ = "730571899"


def all(int_list: list[int], compare: int) -> bool:
    """Checks to see if all the numbers in the list are the same as a specified number."""
    idx: int = 0
    list_len: int = len(int_list)
    count: int = 0

    while (idx < list_len):
        if (int_list[idx] == compare):
            count += 1
            idx += 1
        else:
            return False
        if (count == list_len):
            return True
        
    return False
        

def max(int_list: list[int]) -> int:
    """Finds the maximum value in the list."""
    if (len(int_list) == 0):
        raise ValueError("max() arg is an empty List")
    
    max_int: int = int_list[0]
    idx: int = 0

    while (idx < len(int_list)):
        if (int_list[idx] > max_int):
            max_int = int_list[idx]
        idx += 1

    return max_int


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks to see if each list is the same, both length and in content."""
    idx: int = 0

    if (len(list1) == len(list2)):
        while (idx < len(list1)):
            if (list1[idx] != list2[idx]):
                return False
            idx += 1
    else:
        return False
    
    return True
"""EX05 - Implementing common algorithms to use as subjects for testing."""

__author__: str = "730390832"


def only_evens(haystack: list[int]) -> list[int]: 
    """Generated a list with only even integers."""
    i: int = 0
    all_even: list[int] = []
    while i < len(haystack):
        # if number is divisiable by 2 without remainders, it is an even number.
        if haystack[i] % 2 == 0:
            # adds even number to end of list.
            all_even.append(haystack[i])
        # iterates through next list item.
        i += 1
    # returns only even integers.
    return all_even


def concat(a: list[int], b: list[int]) -> list[int]:
    """Generate a new list of all items of the first list followed by the second."""
    c: list[int] = []
    i: int = 0
    # adds all elements of a to list c.
    c += a
    while i < len(b):
        # add individual elements of list b manually.
        c.append(b[i])
        # iterates through each element of list b. 
        i += 1
    # returns concatenated list. 
    return c


def sub(a_list: list[int], start_i: int, end_i: int) -> list[int]:
    """Generate subset of given list within start index and end index -1."""
    c: list[int] = []
    i: int = 0 
    while i < len(a_list):
        # only append elements to list c if current index is within start_i and end_i-1.
        # retruns empty list if len(a_list) is 0, start is greater than len(a_list), or end is 0. 
        if i >= start_i and i <= (end_i - 1):
            c.append(a_list[i])
        i += 1
    # return subset of the list. 
    return c
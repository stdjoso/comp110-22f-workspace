"""Using lists to implement common algorithms."""

__author__: str = "730390832"


def all(haystack: list[int], needle: int) -> bool:
    """Given a lists of ints, function returns bool indicatiing whether or not all the ints in the list are the same as the given integer."""
    # start from first index
    i: int = 0 
    # return bool statement 
    int_exists_all: bool = True 
    # loop through each index of list 
    if len(haystack) == 0:
        int_exists_all = False
    else:
        while int_exists_all is True and i < len(haystack):
            # if needle(int) is not at Xth index of haystack(list), then automatically false
            if haystack[i] != needle:
                int_exists_all = False 
            # if it is at Xth index, int_exists_all remains True
            else:
                # goes to next index
                i += 1
    return int_exists_all


def max(haystack: list[int]) -> int:
    """Given a list of ints, function returns the largest integer in the list."""
    if len(haystack) == 0:
        # if the list is empty, ValueError is raised
        raise ValueError("max() arg is an empty List")
    # set max variable to an item in the haystack(list)
    max: int = haystack[0]
    # set variable that keeps track of current index of list
    i: int = 0
    while i < len(haystack):
        if haystack[i] > max:
            max = haystack[i]
        i += 1
    # returns max 
    return max 


def is_equal(a: list[int], b: list[int]) -> bool:
    """Given two lists of ints, function returns bool that states if every element at every index is equal in both lists."""
    # start from first index of lists a,b
    i: int = 0
    # return bool statement 
    deep_equality: bool = True
    # loop through each item of list so long as deep_equality remains True
    # and counter is less than len of each list
    if len(a) != len(b):
        deep_equality = False
    else:
        while deep_equality is True and i < len(a) and i < len(b):
            # if len(a) is not equal to len(b), then automatically false
            # if needle(int) is not at Xth index of haystack(list), then automatically false
            if a[i] != b[i]:
                deep_equality = False
            else:
                # goes to next index
                i += 1
    return deep_equality
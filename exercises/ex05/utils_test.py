"""EX05 - Tests for the only_evens, concat, and sub functions."""

__author__: str = "730390832"


from utils import only_evens, sub, concat


# edge case
def test_only_evens_empty() -> None:
    """Test only_evens for empty list."""
    haystack: list[int] = []
    assert (only_evens(haystack)) == []


# use case 1
def test_only_evens_many_items() -> None:
    """Test only_evens for many items in list."""
    haystack: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert (only_evens(haystack)) == [2, 4, 6, 8, 10]


# use case 2
def test_only_evens_all_odds() -> None:
    """Test only_evens for only odd items in list."""
    haystack: list[int] = [9, 27, 43, 87, 41]
    assert (only_evens(haystack)) == []


# edge case 
def test_concat_a_empty() -> None:
    """Test concat for empty list in first paremeter."""
    a: list[int] = []
    b: list[int] = [20, 30, 40]
    assert (concat(a, b)) == [20, 30, 40]


# use case 1 
def test_concat_many_items_numerical_order() -> None:
    """Test concat for concatenating initilaized lists in numerical order."""
    a: list[int] = [1, 2, 3, 4, 5]
    b: list[int] = [6, 7, 8, 9, 10]
    assert (concat(a, b)) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# use case 2
def test_concat_many_items_2() -> None:
    """Test concat for concatenating separate literal list items in numerical order."""
    assert (concat([-2, -1, 0], [1, 2, 3])) == [-2, -1, 0, 1, 2, 3]


# edge case
def test_sub_negative_start_index() -> None:
    """Test sub for negative start index."""
    a_list: int[list] = [1, 2, 3, 4, 5]
    start_i: int = -2
    end_i: int = 4
    assert (sub(a_list, start_i, end_i)) == [1, 2, 3, 4]


# use case 1
def test_sub_many_items() -> None:
    """Test sub for initialized list with multiple items; initialized start and end inidex."""
    a_list: list[int] = [-2, -1, 0, 1, 2, 0]
    start_i: int = 3
    end_i: int = 5
    assert (sub(a_list, start_i, end_i)) == [1, 2]


# use case 2
def test_sub_many_items_2() -> None:
    """Test sub for literal list items; literal start and end index."""
    assert (sub([7, 8, 9, 10, 11, 12], 3, 6)) == [10, 11, 12]

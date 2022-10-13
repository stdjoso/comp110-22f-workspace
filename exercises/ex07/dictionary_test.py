"""Testing Dictionary Functions."""

__author__: str = "730390832"

from dictionary import invert, count, favorite_color


# edge case
def test_invert_empty_input_dictionary() -> None:
    """Test invert() for no key-value pairs in input dictionary."""
    in_dict: dict[str, str] = {}
    assert invert(in_dict) == {}


# use case 1
def test_invert_many_unique_key_value_pairs() -> None:
    """Test invert() for initialized input dictionary with many unique key-value pairs."""
    in_dict: dict[str, str] = {"blue": "color", "circle": "shape", "smooth": "texture"}
    assert invert(in_dict) == {"color": "blue", "shape": "circle", "texture": "smooth"}


# use case 2
def test_invert_many_unique_key_value_pairs_2() -> None:
    """Test invert() for initialized literal input dictionary with many unique key-value pairs."""
    assert invert({"chicken": "protein", "bread": "carbs", "oil": "fats"}) == {"protein": "chicken", "carbs": "bread", "fats": "oil"}


# edge case
def test_count_empty_list() -> None:
    """Test count() for empty input list."""
    assert count([]) == {}


# use case 1
def test_count_unique_frequencies() -> None:
    """Test count() for input list with unique freqencies for each item."""
    input_list: list[str] = ["apple", "pear", "pear", "orange", "orange", "orange"]
    assert count(input_list) == {"apple": 1, "pear": 2, "orange": 3}


# use case 2
def test_count_variable_frequencies() -> None:
    """Test count() for input list with some similar frequencies for each item."""
    input_list: list[str] = ["peanut", "hazelnut", "almond", "peanut", "cashew", "hazelnut"]
    assert count(input_list) == {"peanut": 2, "hazelnut": 2, "almond": 1, "cashew": 1}


# edge case
def test_favorite_colors_empty_input_dict() -> None:
    """Test favorite_colors() for empty input dict."""
    assert favorite_color({}) == ""


# use case 1
def test_favorite_colors_multiple_max() -> None:
    """Test favorite_colors() for input dict with more than one mode color."""
    names_and_col: dict[str, str] = {"Sam": "blue", "Kenz": "blue", "Steph": "purple", "Won": "purple", "Matt": "green"}
    assert favorite_color(names_and_col) == "blue"


# use case 2
def test_favorite_colors_unique_max() -> None:
    """Test favorite_colors() for input dict with unique mode color."""
    names_and_col: dict[str, str] = {"Sam": "red", "Kenz": "blue", "Steph": "red", "Won": "red", "Matt": "green", "Sophie": "green"}
    assert favorite_color(names_and_col) == "red"
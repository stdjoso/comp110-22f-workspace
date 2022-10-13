"""Using Dictionaries to Execute Common Functions."""

__author__: str = "730390832"


def invert(in_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a given dictionary."""
    # return a dictionary that inverts the keys and values 
    out_dict: dict[str, str] = {}
    # the keys of the input list becomes the values of the output list 
    for key in in_dict:
        value: str = in_dict[key]   
        out_dict[value] = key   
    # raise value error if you encounter one of the same in value//out key
    if len(out_dict) != len(in_dict):
        raise KeyError("input dict() has duplicate values!")
    else: 
        return out_dict


def favorite_color(names_and_col: dict[str, str]) -> str:
    """Returns most frequently occurring color vlaue given a dictionary keyed with names."""
    # initialize color storage dict
    color_dict: dict[str, int] = {}
    # iterate through each item in input dictionary
    for name in names_and_col:
        # if color is founf in storage dict, increase count / frequency value
        if names_and_col[name] in color_dict:
            color_dict[names_and_col[name]] += 1
        else:     # if list item is found for the first time, set inital count of 1
            color_dict[names_and_col[name]] = 1
    max: int = 0      # initialize max int value 
    freq_color: str = ""     # result storage 
    for color in color_dict:     # max function for..in loop (recall utils)
        if color_dict[color] > max:     
            max = color_dict[color]
            freq_color = color
    return freq_color      # returns str which is the color that occurs most frequently


def count(input_list: list[str]) -> dict[str, int]:
    """Generate dictionary where key-value pair is unique list item-frequency / count."""
    # initialize empty dict to store result 
    count_list_dict: dict[str, int] = {}
    # iterate through each item in input list
    for item in input_list:
        # if list item is found in result dict, increase count / frequency value
        if item in count_list_dict:
            count_list_dict[item] += 1
        else:      # if list item is found for the first time, set inital count of 1
            count_list_dict[item] = 1
    return count_list_dict     # returns result dict with list item-frequency pairs
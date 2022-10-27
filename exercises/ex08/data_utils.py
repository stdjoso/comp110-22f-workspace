"""Dictionary related utility functions."""

__author__: str = "730390832"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read enitre CSV of data into a list of rows / 'table'."""
    result: list[dict[str, str]] = []
    # Open a handle to the data file 
    file_handle = open(filename, "r", encoding="utf8")
    # Prepare to read the data file as a CSV rather than just strings 
    csv_reader = DictReader(file_handle)
    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)
    # Close the file when we're done, to free its resources
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list of all the values in a specified column."""
    column_values: list[str] = []
    for row in table:
        item: str = row[column]
        column_values.append(item)
    return column_values


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table form row-orientation to column-oriented table."""
    col_table: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        col_table[column] = column_values(row_table, column)
    return col_table


def head(col_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a column-oriented table with only the specificed rows of data for each column."""
    result: dict[str, list[str]] = {}
    # loop through each of the columns in the n row of the table
    for key in col_table:
        # establish empty list to sore each of the first n values in the column
        col_n_values: list[str] = []
        # if n is too big, assigns n to number of rows in column / 'length'
        if n > len(col_table[key]):
            n = len(col_table[key])
        # loop through the first n items of the table's column
        for value in range(0, n):
            # append each item to the list 
            col_n_values.append(col_table[key][value])
        # assign list of column values to the result dict 
        result[key] = col_n_values
    return result


def select(column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:  
    """Produce a column-oriented table with a specified subset of the orginal columns."""
    subset: dict[str, list[str]] = {}
    # loop through each of the column in the second parameter of the function
    for key in column_names:
        # assign to the column key of the result dictionary the list of values stored in the input dictionary at the same column
        subset[key] = column_table[key]
    # return the dictionary produced
    return subset


def concat(col_table_1: dict[str, list[str]], col_table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a column-oriented table with two column-oriented tabled combined."""
    combined_col_table: dict[str, list[str]] = {}
    # loop through each of the columns in the first parameter of the function
    for column in col_table_1:
        # assign to the column key of the result dictionary the list of values stored in the first parameter at the same column
        combined_col_table[column] = col_table_1[column]
    # loop through each of the columns in the second paramter of the function 
    for column in col_table_2:
        # if the current column key is already in the result ditionary, add on to the list of values stored in the second paramter at the same column 
        if column in combined_col_table:
            combined_col_table[column] += col_table_2[column]
        # otherwise, assign to the column key of the result dictionary the list of values stored in the second paramter at the same column
        else:
            combined_col_table[column] = col_table_2[column]
    return combined_col_table


def count(freq_list: list[str]) -> dict[str, int]:
    """Generate dictionary where key-value pair is unique list item-frequency / count."""
    count_dict: dict[str, int] = {}
    # loop through each item of the input list
    # check to see if that item has already been established as a key error in your 
    # dictionary. try bool conditional
    for item in freq_list:
        if item in count_dict:
            # if the name is found in the dict, that means there is already a key-value
            # pair where the item is a key. increase the value associated with that key by 1
            count_dict[item] += 1
        # if the item is not found in the dict, that means it is the fisrt time encountering it.
        # assign initial count of 1. 
        else:
            count_dict[item] = 1
    return count_dict
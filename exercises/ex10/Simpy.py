"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__: str = "730390832"


class Simpy:
    """A list of floats values."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initialize Simpy Class with list of float values."""
        self.values = values

    def __repr__(self) -> str:
        """Produces str representation of Simpy Class."""
        return f"Simpy({self.values})"

    def fill(self, repeat_values: float, frequency: int) -> None:
        """Fill values attribute with a specfic number of repreating values."""
        self.values = []       
        for _ in range(frequency):
            self.values.append(repeat_values)
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill values attribute with a range of values."""
        assert step != 0.0
        self.values = []         
        while abs(start) < abs(stop):       
            self.values.append(start)
            start += step

    def sum(self) -> float:
        """Computes and returns sum of all itens in the values attribute."""
        total: float = 0.0
        total = sum(self.values)
        return total
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Addition operator overload."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            # loop through items in list
            for value in self.values:
                # append the concat. string to result item list 
                result.values.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            # loop through each index of self's items
            for i in range(len(self.values)):
                # append resulting string to result item list
                result.values.append(self.values[i] + rhs.values[i])
        return result 

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Exponentiation operator overload."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        return result 

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Equality operator overload that returns boolean mask."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                if value == rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Greater-than operator overload that returns boolean mask."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                if value > rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result
        
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Subsription notation operator overload that returns filtered items."""
        if isinstance(rhs, int):
            result_float: float = 0.0
            result_float = self.values[rhs]
            return result_float
        else:
            result_simpy: Simpy = Simpy([])
            for i in range(len(self.values)):
                if rhs[i] is True:
                    result_simpy.values.append(self.values[i])
            return result_simpy 
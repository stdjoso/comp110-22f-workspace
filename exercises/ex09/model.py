"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__: str = "730390832"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:              # Point#distance
        """Returns distance between two points."""
        distance: float = 0.0
        # distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        distance = sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
        return distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = 0

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Establishes cell location with every tick."""
        self.location = self.location.add(self.direction)
        # if a Cell is infected, sickness += 1
        if self.is_infected() is True:
            self.sickness += 1
        # if Cell.sickness > RECOVERY_PERIOD, cell is immunized
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()

    def color(self) -> str:
        """Return the color representation of a cell."""
        # if cell is vulnerable, return gray
        if self.is_vulnerable() is True:
            return "gray"
        # if cell is infected, return different color turtle name
        elif self.is_infected() is True:
            return "orchid"
        # if cell is immune, return different color turtle name
        elif self.is_immune() is True:
            return "powder blue"

    def contract_disease(self) -> None:             # Cell#contract_disease
        """Updates cell sickness to infected."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:            # Cell#is_vulnerable
        """Accesses sickness attribute to determine if cell is not infected."""
        if self.sickness == constants.VULNERABLE:
            return True 
        else: 
            return False 

    def is_infected(self) -> bool:              # Cell#is_infected
        """Accesses sickness attribute to determine if cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else: 
            return False

    def contact_with(self, contact_cell: Cell) -> None:                 # Cell#contact_with
        """Cells that come in contact remain vulnerable or become infected."""
        if self.is_vulnerable() is True and contact_cell.is_infected() is True:
            self.contract_disease()
        if contact_cell.is_vulnerable() is True and self.is_infected() is True:
            contact_cell.contract_disease()

    def immunize(self) -> None:             # Cell#immunize
        """Updates cell sickness to immune."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> bool:            # Cell#is_immune
        """Access sickness attribute to determine if cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int, immune: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        # if 'infected' parameter is equal to or exceeds the value of 'cells' parameter,
        # or is 0 or negative, or 'immune' is greater than 'cells', raise a ValueError
        if infected >= cells or infected <= 0:
            raise ValueError("Some number of the 'Cell' objects must begin infected, but not all.")
        elif immune >= cells or immune < 0:
            raise ValueError("Not all 'Cell' objects can begin immunized.")
        elif immune < 0:
            raise ValueError("Number of immune 'Cell' objects out of bounds.")
        # use _ for variable that is not referenced in loop 
        # range includes vulnerable cells only 
        for _ in range(cells - infected - immune):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            # only vulnerable cells appended
            self.population.append(cell)
        # range includes infected cells only 
        for _ in range(infected):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            infected_cell: Cell = Cell(start_location, start_direction)
            # infected cells contract disease and correct color turtle str 
            infected_cell.contract_disease()
            # only append infected cells
            self.population.append(infected_cell)
        # range includes immune cells only 
        for _ in range(immune):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            immune_cell: Cell = Cell(start_location, start_direction)
            # immunized and correct color turtle str
            immune_cell.immunize()
            # only append immune cells
            self.population.append(immune_cell)

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        # check for contacts once every time method is called. 
        self.check_contacts()
        
    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:              # Model#check_contacts
        """Test if two Cells come in contact."""
        for cell in self.population:
            i: int = 0 
            while i < len(self.population):
                if self.population[i].location.distance(cell.location) < constants.CELL_RADIUS:
                    cell.contact_with(self.population[i])
                i += 1
    
    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        is_complete: bool = False
        i: int = 0 
        while i < len(self.population):
            # if all cells are immune or vulnerable, the simulation is complete 
            if self.population[i].is_immune() is True or self.population[i].is_vulnerable() is True:
                is_complete = True
                i += 1
            else:
                # automatically false if cell is not immune or vulnerable
                return False 
        return is_complete
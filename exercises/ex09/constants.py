"""Constants used through the simulation."""

BOUNDS_WIDTH: int = 400
MAX_X: float = BOUNDS_WIDTH / 2
MIN_X: float = -MAX_X
VIEW_WIDTH: int = BOUNDS_WIDTH + 20

BOUNDS_HEIGHT: int = 400
MAX_Y: float = BOUNDS_HEIGHT / 2
MIN_Y: float = -MAX_Y
VIEW_HEIGHT: int = BOUNDS_HEIGHT + 20

CELL_RADIUS: int = 15
CELL_COUNT: int = 20
CELL_SPEED: float = 5.0

# new constants 
VULNERABLE: int = 0
INFECTED: int = 1
INFECTED_COUNT: int = 5
IMMUNE: int = -1
RECOVERY_PERIOD: int = 90
IMMUNE_COUNT: int = 2
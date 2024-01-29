from src.orientation import Orientation
from src.coordinate import Coordinate
from src.ship import Ship


class ShipPlacement(object):
    def __init__(self, the_ship: Ship, ori: Orientation, start: Coordinate) -> None:
        self.the_ship = the_ship
        self.orientation = ori
        self.start_coord = start
        self.end_coord = self.get_end_coord()

    def get_end_coord(self) -> Coordinate:
        if self.orientation == Orientation.VERTICAL:
            return Coordinate(self.start_coord.row + self.the_ship.length - 1, self.start_coord.col)
        elif self.orientation == Orientation.HORIZONTAL:
            return Coordinate(self.start_coord.row, self.start_coord.col + self.the_ship.length - 1)
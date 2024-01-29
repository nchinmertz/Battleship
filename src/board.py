from typing import Iterator, List, overload, Tuple
from src.cell import Cell
from src.coordinate import Coordinate
from src.ship_placement import ShipPlacement
from src.real_errors import ShipPlacementError, MoveError
from src.ship import Ship


class Board(object):
    contents: List[List[Cell]]

    def __init__(self, num_rows: int, num_cols: int, blank_char: str) -> None:
        self.contents = [[Cell(blank_char) for col in range(num_cols)] for row in range(num_rows)]
        self.blank_char = blank_char

    def num_rows(self) -> int:
        return len(self.contents)

    def num_cols(self) -> int:
        return len(self[0])

    def get_display(self, visibility: bool) -> str:
        sep = ' ' * max([len(str(self.num_rows())), len(str(self.num_cols()))])
        rep = sep*2 + sep.join((str(i) for i in range(self.num_cols()))) + '\n'
        for row_index, row in enumerate(self):
            row = [cur_cell.display(visibility) for cur_cell in row]
            rep += str(row_index) + sep + sep.join(row) + '\n'
        return rep

    def __str__(self) -> str:
        sep = ' ' * max([len(str(self.num_rows())), len(str(self.num_cols()))])
        rep = sep * 2 + sep.join((str(i) for i in range(self.num_cols()))) + '\n'
        for row_index, row in enumerate(self):
            rep += str(row_index) + sep + sep.join(row) + '\n'
        return rep

    def __iter__(self) -> Iterator[List[Cell]]:
        return iter(self.contents)

    @overload
    def __getitem__(self, index: int) -> List[Cell]:
        ...

    @overload
    def __getitem__(self, coord: Coordinate) -> Cell:
        ...

    def __getitem__(self, location):
        if isinstance(location, int):
            return self.contents[location]
        elif isinstance(location, Coordinate):
            return self.contents[location.row][location.col]

    def is_in_bounds(self, row: int, col: int) -> bool:
        return (0 <= row < self.num_rows() and
                0 <= col < self.num_cols())

    def add_ship(self, ship_placement: ShipPlacement, ship_name: Ship) -> None:
        start = ship_placement.start_coord
        end = ship_placement.end_coord
        ori = ship_placement.orientation
        if not self.is_in_bounds(start.row, start.col):
            if ori == ori.VERTICAL:
                raise ShipPlacementError(f'Cannot place {ship_name} vertically at {start.row}, {start.col} because it would be out of bounds.')
            if ori == ori.HORIZONTAL:
                raise ShipPlacementError(f'Cannot place {ship_name} horizontally at {start.row}, {start.col} because it would be out of bounds.')
        if not self.is_in_bounds(end.row, end.col):
            if ori == ori.VERTICAL:
                raise ShipPlacementError(f'Cannot place {ship_name} vertically at {end.row-1}, {end.col} because it would end up out of bounds.')
            if ori == ori.HORIZONTAL:
                raise ShipPlacementError(f'Cannot place {ship_name} horizontally at {end.row}, {end.col-1} because it would end up out of bounds.')

        conflicting_ships = self.get_ships_contained_between(start, end)
        if conflicting_ships:
            if ori == ori.VERTICAL:
                raise ShipPlacementError(f'Cannot place {ship_name} vertically at {start.row}, {start.col} because it would overlap with {conflicting_ships}')
            if ori == ori.HORIZONTAL:
                raise ShipPlacementError(f'Cannot place {ship_name} horizontally at {start.row}, {start.col} because it would overlap with {conflicting_ships}')

        for row in range(start.row, end.row + 1):
            for col in range(start.col, end.col + 1):
                self[row][col].contents = ship_placement.the_ship.initial

    def hit(self, firing_location: Coordinate) -> None:
        if not self.is_in_bounds(firing_location.row, firing_location.col):
            raise MoveError(f'{firing_location.row}, {firing_location.col} is not in bounds of our {self.num_rows()} X {self.num_cols()} board.')
        elif self[firing_location].has_been_fired_at():
            raise MoveError(f'You have already shot at {firing_location.row}, {firing_location.col}')
        else:
            self[firing_location].get_hit()

    def get_ships_contained_between(self, start: Coordinate, end: Coordinate) -> List[str]:
        conflicting_ships = set()
        for row in range(start.row, end.row + 1):
            for col in range(start.col, end.col + 1):
                if self[row][col].contains_ship():
                    conflicting_ships.add(self[row][col].contents)
        return sorted(conflicting_ships)

    def get_empty_fire_coordinates(self) -> List[Tuple[int, int]]:
        empty_fire_coords = []
        for row in range(self.num_rows()):
            for col in range(self.num_cols()):
                if not self[row][col] == self.blank_char:
                    empty_fire_coords.append((row, col))
        return empty_fire_coords

    def comp_hit(self, firing_location: Coordinate) -> None:
        self[firing_location].get_hit()



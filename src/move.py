from src.coordinate import Coordinate
from src.real_errors import CoordinateError, MoveError
from src.player import Player


class Move(object):
    def __init__(self, maker: "Player", firing_location: Coordinate) -> None:
        self.maker = maker
        self.firing_location = firing_location

    @classmethod
    def from_str_fire(cls, maker: "Player", str_rep: str) -> "Move":
        try:
            firing_coord = Coordinate.from_string_fire(str_rep)
            return Move(maker, firing_coord)
        except CoordinateError as error:
            raise MoveError(str(error))

    def make(self) -> None:
        self.maker.shoot(self.firing_location)


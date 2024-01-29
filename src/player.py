from typing import List, Iterable, Optional
import copy
from src.board import Board
from src.game_config import GameConfig
from src.orientation import Orientation
from src.coordinate import Coordinate
from src.real_errors import ShipPlacementError, MoveError, OrientationError, CoordinateError
import abc
from src.ship import Ship

# Set a player to have ships, a board, and an opponent
# There are many different types of players,
# Each player gets input and make moves differently
# Therefore this class get inherited to human player and computer player


class Player(abc.ABC):
    def __init__(self, config: GameConfig, players: Iterable['Player']) -> None:
        self.name = self.get_name(players)
        ships = copy.deepcopy(config.ships)
        self.ships = {ship.initial: ship for ship in ships}  # dictionary of ships
        self.board = Board(config.num_rows, config.num_cols, config.blank_char)
        self.opponent = None
        self.place_ships()

    @staticmethod
    def player_num(i=[0]):  # if two of the same type is used they have different names, ie CheatingAi1 and CheatingAi2
        i[0] += 1
        return i[0]

    def take_turn(self) -> None:
        self.display_game_state()
        while True:
            try:
                my_move = self.get_move(self.board, self)
                my_move.make()
                return
            except MoveError as error:
                print(error)

    def all_ships_destroyed(self) -> bool:
        return all((_ship.is_destroyed() for _ship in self.ships.values()))

    @abc.abstractmethod
    def place_ships(self) -> None:
        ...

    @abc.abstractmethod
    def get_name(self, players: Iterable['Player']):
        ...

    @abc.abstractmethod
    def place_ship(self, _ship: Ship) -> None:
        ...

    def __str__(self) -> str:
        return self.name

    @abc.abstractmethod
    def get_ship_orientation(self, _ship: Ship):
        ...

    @abc.abstractmethod
    def get_ship_start_coords(self, _ship: Ship, orientation: Orientation):
        ...

    @abc.abstractmethod
    def get_ship_placement(self, _ship: Ship):
        ...

    @abc.abstractmethod
    def get_move(self, board: Board):
        ...

    def shoot(self, firing_location: Coordinate):
        self.opponent.get_shot(firing_location)

    @abc.abstractmethod
    def get_shot(self, firing_location: Coordinate) -> None:
        ...

    def display_game_state(self) -> None:
        print(f"{self.name}'s Scanning Board")
        print(self.opponent.board.get_display(False))
        print(f"{self.name}'s Board")
        print(self.board.get_display(True))

    def display_cur_player_game_state(self) -> None:
        print(f"{self.opponent.name}'s Scanning Board")
        print(self.board.get_display(False))
        print(f"{self.opponent.name}'s Board")
        print(self.opponent.board.get_display(True))

import random
from typing import Iterable, List
from src.ship import Ship
from src.orientation import Orientation
from src.player import Player
from src.ship_placement import ShipPlacement
from src.coordinate import Coordinate
from src.game_config import GameConfig
import abc
from src.real_errors import ShipPlacementError
from src.board import Board

# The whole set up process is the same for each computer player
# The only difference is how they are going to play the game
# Therefore another layer of inheritance needs to occur

class ComputerPlayer(Player):
    def __init__(self, config: GameConfig, players: Iterable['Player']):
        super().__init__(config, players)

    def place_ships(self) -> None:
        print(f"{self}'s Placement Board")
        print(self.board.get_display(True))
        for my_ship in self.ships.values():
            self.place_ship(my_ship)

    def place_ship(self, ship_: Ship) -> None:
        placement = self.get_ship_placement(ship_)
        while True:
            try:
                self.board.add_ship(placement, ship_.name)
                print(f"{self}'s Placement Board")
                print(self.board.get_display(True))
                break
            except ShipPlacementError:
                placement = self.get_ship_placement(ship_)

    def get_ship_orientation(self, ship_: Ship) -> Orientation:
        return random.choice([Orientation.HORIZONTAL, Orientation.VERTICAL])

    def get_ship_start_coords(self, ship_: Ship, orientation_: Orientation) -> Coordinate:
        if orientation_ == Orientation.HORIZONTAL:
            row = random.randint(0, self.board.num_rows() - 1)
            col = random.randint(0, self.board.num_cols() - ship_.length)
        else:
            row = random.randint(0, self.board.num_rows() - ship_.length)
            col = random.randint(0, self.board.num_cols() - 1)
        return Coordinate(row, col)

    def get_ship_placement(self, _ship: Ship) -> ShipPlacement:
        placement_orientation = self.get_ship_orientation(_ship)
        start_coords = self.get_ship_start_coords(_ship, placement_orientation)
        return ShipPlacement(_ship, placement_orientation, start_coords)

    @abc.abstractmethod
    def get_name(self, players: Iterable['Player']):
        ...

    @abc.abstractmethod
    def get_move(self, board: Board, player: Player):
        ...

    def get_shot(self, firing_location: Coordinate) -> None:
        self.board.comp_hit(firing_location)
        location = self.board[firing_location]  # returns true if ship is contained at coord
        if location.contains_ship():
            ship_hit = self.ships[location.contents]
            ship_hit.receive_hit()
            print(f"You hit {self.name}'s {ship_hit}!")
            if ship_hit.is_destroyed():
                print(f"You destroyed {self.name}'s {ship_hit}")
        else:
            print('Miss')
        self.display_cur_player_game_state()



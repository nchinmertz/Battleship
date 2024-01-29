from typing import Iterable
from src.player import Player
from src.orientation import Orientation
from src.ship_placement import ShipPlacement
from src.game_config import GameConfig
from src.coordinate import Coordinate
from src.real_errors import CoordinateError, OrientationError, ShipPlacementError
from src.move import Move
from src.board import Board
from src.ship import Ship


# inherited from player, the main change is user input is needed to play the game
class HumanPlayer(Player):
    def __init__(self, config: GameConfig, players: Iterable['Player']):
        super().__init__(config, players)

    def place_ships(self) -> None:
        for my_ship in self.ships.values():
            self.place_ship(my_ship)
        print(f"{self}'s Placement Board")
        print(self.board.get_display(True))

    def place_ship(self, _ship: Ship) -> None:
        print(f"{self}'s Placement Board")
        print(self.board.get_display(True))
        while True:
            try:
                ship_placement = self.get_ship_placement(_ship)
                self.board.add_ship(ship_placement, _ship.name)
                return
            except ShipPlacementError as error:
                print(error)

    def get_name(self, players: Iterable['Player']) -> str:
        already_used_names = set([player.name for player in players])
        while True:
            name = input(f'Player {self.player_num()} please enter your name: ')
            if name not in already_used_names:
                return name
            else:
                print(f'Someone is already using {name} for their name.\nPlease choose another name.')

    def get_ship_orientation(self, _ship: Ship):
        while True:
            try:
                orientation = Orientation.from_string(input(
                    f'{self.name} enter horizontal or vertical for the orientation of {_ship} which is {_ship.length} long: '))
                return orientation
            except OrientationError as error:
                print(error)

    def get_ship_start_coords(self, _ship: Ship, orientation: Orientation) -> Orientation:
        num_rows = self.board.num_rows()
        num_cols = self.board.num_cols()
        while True:
            try:
                coords = Coordinate.from_string(input(
                    f'{self.name}, enter the starting position for your {_ship} ship ,which is {_ship.length} long, in the form row, column: '), num_rows, num_cols)
                return coords
            except CoordinateError as error:
                print(error)

    def get_ship_placement(self, _ship: Ship) -> ShipPlacement:
        orientation = self.get_ship_orientation(_ship)
        start_coords = self.get_ship_start_coords(_ship, orientation)
        return ShipPlacement(_ship, orientation, start_coords)

    def get_move(self, board: Board, player) -> 'move.Move':
        return Move.from_str_fire(self, input(f'{self.name}, enter the location you want to fire at in the form row, column: '))

    def get_shot(self, firing_location: Coordinate) -> None:
        self.board.hit(firing_location)
        location = self.board[firing_location]  # returns true if ship is contained at given coordinate, aka a hit
        if location.contains_ship():
            ship_hit = self.ships[location.contents]
            ship_hit.receive_hit()
            print(f"You hit {self.name}'s {ship_hit}!")
            if ship_hit.is_destroyed():
                print(f"You destroyed {self.name}'s {ship_hit}")
        else:
            print('Miss')
        self.display_cur_player_game_state()

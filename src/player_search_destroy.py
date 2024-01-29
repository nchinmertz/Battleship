from typing import Iterable, Tuple, List
from src.player_computer import ComputerPlayer
from src.game_config import GameConfig
from src.player import Player
from src.board import Board
import random
from src.move import Move

# Will act like a random player until it makes a hit, then it will hit all the spaces around the valid hit


class SearchDestroyComputer(ComputerPlayer):
    def __init__(self, config: GameConfig, players: Iterable['Player']):
        super().__init__(config, players)
        self.possible_coords = self.board.get_empty_fire_coordinates()
        self.destroy_mode = False
        self.destroy_mode_cords = []
        self.opponent_ship_coords = []

    def get_name(self, players: Iterable['Player']):
        return f'Search Destroy {self.player_num()}'

    def get_move(self, the_board: Board, player: Player) -> 'Move':
        if len(self.destroy_mode_cords) == 0:
            coo = random.choice(self.possible_coords)
            row = coo[0]
            col = coo[1]
            self.possible_coords.remove(coo)
            coordinates = str(row) + ',' + str(col)
            if coo in self.get_opponent_ship_cords(player):
                self.destroy_mode = True
                self.destroy_mode_start(int(row), int(col))
            return Move.from_str_fire(self, coordinates)
        else:
            if len(self.destroy_mode_cords) != 0:
                coo = self.destroy_mode_cords.pop(0)
                row = coo[0]
                col = coo[1]
                if coo in self.get_opponent_ship_cords(player):
                    row = coo[0]
                    col = coo[1]
                    self.destroy_mode_start(row, col)
                coordinates = str(row) + ',' + str(col)
                return Move.from_str_fire(self, coordinates)
            else:
                self.destroy_mode = False

    def destroy_mode_start(self, row: int, col: int) -> None:  # Activates once a hit has happened
        self.destroy_mode = True
        destroy_queue = [(row, col-1), (row-1, col), (row, col+1), (row+1, col)]
        for coord in destroy_queue:
            if coord in self.possible_coords:
                self.destroy_mode_cords.append(coord)
                self.possible_coords.remove(coord)

    def get_opponent_ship_cords(self, players: Player) -> List[Tuple[int, int]]:
        for row in range(self.board.num_rows()):
            for col in range(self.board.num_cols()):
                if players.opponent.board[row][col].contains_ship() and not players.opponent.board[row][col].has_been_fired_at():
                    self.opponent_ship_coords.append((row, col))
        return self.opponent_ship_coords

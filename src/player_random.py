from typing import Iterable
from src.player_computer import ComputerPlayer
from src.game_config import GameConfig
from src.player import Player
from src.move import Move
from src.board import Board
import random

# This just makes random hits that haven't been hit yet


class RandomComputer(ComputerPlayer):
    def __init__(self, config: GameConfig, players: Iterable['Player']):
        super().__init__(config, players)
        self.empty_coord = self.board.get_empty_fire_coordinates()

    def get_name(self, players: Iterable['Player']):
        return f'Random {self.player_num()}'

    def get_move(self, board: Board, player: Player) -> 'Move':
        coo = random.choice(self.empty_coord)
        row = coo[0]
        col = coo[1]
        self.empty_coord.remove(coo)
        coordinates = str(row) + ',' + str(col)
        return Move.from_str_fire(self, coordinates)

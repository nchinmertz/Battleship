from typing import Iterable, List, Tuple
from src.player_computer import ComputerPlayer
from src.player import Player
from src.game_config import GameConfig
from src.board import Board
from src.move import Move

# The cheating player has access to their opponent's ship placements


class CheatingPlayer(ComputerPlayer):
    def __init__(self, config: GameConfig, players: Iterable['Player']):
        super().__init__(config, players)
        self.opponent_ship_coords = []  # Where other player's ship coordinates are

    def get_name(self, players: Iterable['Player']):
        return f'Cheating {self.player_num()}'

    def get_move(self, the_board: Board, players: Player) -> 'Move':
        for row in range(self.board.num_rows()):
            for col in range(self.board.num_cols()):
                if players.opponent.board[row][col].contains_ship() and not players.opponent.board[row][col].has_been_fired_at():
                    self.opponent_ship_coords.append((row, col))
                    self.opponent_ship_coords.sort()
                    cord = self.opponent_ship_coords[0]
                    row = cord[0]
                    col = cord[1]
                    self.opponent_ship_coords.remove(cord)
                    coords = str(row) + ',' + str(col)
                    return Move.from_str_fire(self, coords)

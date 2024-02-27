from typing import TypeVar
from src.player import Player
from src.game_config import GameConfig
from src.player_human import HumanPlayer
from src.player_search_destroy import SearchDestroyComputer
from src.player_cheating import CheatingPlayer
from src.player_random import RandomComputer
import random


class Game(object):
    def __init__(self, config_file_path: str = "configs/classic_game.txt", game_seed=542) -> None:
        # The game_seed is an optional parameter used for test randomness so the same "random" numbers are used
        config = GameConfig(config_file_path)
        random.seed(game_seed)
        self.players = []
        for _ in range(2):
            player_type = self.pick_player_type()
            self.players.append(player_type(config, self.players))
        self.players[0].opponent = self.players[1]
        self.players[1].opponent = self.players[0]
        self._cur_player_turn = 0

    def pick_player_type(self, i=[0]) -> 'Player':  # gets the type of players
        possible_players = {'Human': HumanPlayer, 'Cheating': CheatingPlayer,
                            'SearchDestroy': SearchDestroyComputer, 'Random': RandomComputer}
        while True:
            picked_type = input(f"Enter one of {list(possible_players)} for Player {i[0]+1}'s type: ").strip().lower()
            for name, type in possible_players.items():
                if name.lower().startswith(picked_type):  # can just put in the start of the type
                    i[0] += 1  # used to differentiate between player 1 and player 2 when asking for input
                    return type
            else:
                print(f'{picked_type} is not one of {list(possible_players)}')

    def play(self) -> None:
        while True:
            self.cur_player.take_turn()
            if self.is_game_over():  # once game is over, breaks out of loop
                break
            self.change_turn()  # if the game is not over, next person plays
        self.display_the_winner()

    def is_game_over(self) -> bool:  # checks if the game is over by seeing if one player's ships are all destroyed
        return any((player.all_ships_destroyed() for player in self.players))

    def change_turn(self) -> None:
        self._cur_player_turn = (self._cur_player_turn + 1) % 2  # only two people are playing, player one or two

    @property
    def cur_player(self) -> "Player":
        return self.players[self._cur_player_turn]

    def display_the_winner(self):
        print(f'{self.cur_player} won the game!')

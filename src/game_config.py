from src.ship import Ship

# Information from the config_file is read and set up here


class GameConfig(object):
    def __init__(self, config_file_path: str, blank_char:str = '*') -> None:
        with open(config_file_path) as config_file:
            row, col = config_file.readline().strip().split()
            self.blank_char = blank_char
            self.num_rows = int(row)
            self.num_cols = int(col)
            self.ships = []
            for line in config_file:
                ship_name, ship_length = line.split()
                ship_length = int(ship_length)
                self.ships.append(Ship(ship_name, ship_length))
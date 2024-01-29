from src.real_errors import CoordinateError


class Coordinate(object):
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col

    @classmethod
    def from_string(cls, str_rep: str, num_rows, num_cols) -> "Coordinate":
        str_rep = str_rep.strip()
        try:
            row, col = str_rep.split(',')
        except ValueError:
            raise CoordinateError(f'{str_rep} is not in the form x,y')

        try:
            row = int(row)
        except ValueError:
            raise CoordinateError(f'{row} is not a valid value for row.\n'
                                  f'It should be an integer between 0 and {num_rows - 1}')
        try:
            col = int(col)

        except ValueError:
            raise CoordinateError(f'{col} is not a valid value for row.\n'
                                  f'It should be an integer between 0 and {num_cols - 1}')
        return cls(row, col)

    @classmethod
    def from_string_fire(cls, str_rep : str) -> 'Coordinate':
        str_rep = str_rep.strip()
        try:
            row, col = str_rep.split(',')
        except ValueError:
            raise CoordinateError(f'{str_rep} is not a valid location.\n'
                                  f'Enter the firing location in the form row, column')
        try:
            row = int(row)
        except ValueError:
            raise CoordinateError(f'Row should be an integer. {row} is NOT an integer.')
        try:
            col = int(col)

        except ValueError:
            raise CoordinateError(f'Column should be an integer. {col} is NOT an integer.')
        return cls(row, col)



import enum
from src.real_errors import OrientationError


class Orientation(enum.Enum):
    HORIZONTAL = 'horizontal'
    VERTICAL = 'vertical'

    @staticmethod
    def from_string(str_rep: str) -> "Orientation":
        str_rep = str_rep.strip().lower()
        # a is a prefix of b if b starts with a
        for ori in Orientation:
            if ori.value.startswith(str_rep):
                return ori
        raise OrientationError(f'{str_rep} does not represent an Orientation')



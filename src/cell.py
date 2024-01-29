class Cell(object):
    def __init__(self, contents: str, hit_marker: str = 'X',
                 miss_marker: str = 'O', blank_char: str = '*') -> None:
        self.contents = contents
        self.hit_marker = hit_marker
        self.miss_marker = miss_marker
        self.blank_char = blank_char
        self._has_been_fired_at = False

    def display(self, visibility: bool) -> str:
        if visibility: # display for personal board
            if self.has_been_fired_at():
                if self.contains_ship():
                    return self.hit_marker
                else:
                    return self.miss_marker
            else:
                return self.contents
        else:  # display for scanning board
            if self.has_been_fired_at():
                if self.contains_ship():
                    return self.hit_marker
                else:
                    return self.miss_marker
            else:
                return self.blank_char

    def get_hit(self) -> None:
        self._has_been_fired_at = True

    def contains_ship(self) -> bool:
        return self.contents != self.blank_char

    def has_been_fired_at(self) -> bool:
        return self._has_been_fired_at


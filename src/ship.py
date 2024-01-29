
# A class for all the different ships that are being played with
# Keeps all ships in order and checks if they are destroyed or not

class Ship(object):
    def __init__(self, name: str, length: int) -> None:
        self.name = name
        self.length = length
        self.health = length

    @property
    def initial(self):
        return self.name[0]

    def receive_hit(self) -> None:
        self.health -= 1

    def is_destroyed(self) -> bool:
        return self.health == 0

    def __str__(self) -> str:
        return self.name

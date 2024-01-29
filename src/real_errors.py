class ShipPlacementError(Exception):
    ...


class OrientationError(ShipPlacementError):
    ...


class CoordinateError(ShipPlacementError):
    ...


class MoveError(CoordinateError):
    ...

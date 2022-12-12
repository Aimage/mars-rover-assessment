from .compass_point import COMPASS_MAP


class Rover:
    def __init__(self, name: str, x_position: int, y_position: int, direction: str):
        self.name = name
        self.x = x_position
        self.y = y_position
        self.direction = direction

    def __repr__(self):
        return f"{self.name}:{self.x} {self.y} {self.direction}"

    def spin_left(self, compass_point):
        self.direction = compass_point.left

    def spin_right(self, compass_point):
        self.direction = compass_point.right

    def spin(self, direction):
        compass_point = COMPASS_MAP[self.direction]
        if direction == "L":
            self.spin_left(compass_point)
        if direction == "R":
            self.spin_right(compass_point)

    def x_move(self, grid: int):
        self.x += grid

    def y_move(self, grid: int):
        self.y += grid

    def move(self):
        if self.direction == "N":
            self.y_move(1)
        if self.direction == "S":
            self.y_move(-1)
        if self.direction == "E":
            self.x_move(1)
        if self.direction == "O":
            self.x_move(-1)

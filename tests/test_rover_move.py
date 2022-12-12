
from mars_rover.rover import Rover


def test_move_north():
    rover = Rover("rover1", 1, 2, "N")
    rover.move()
    assert(rover.x == 1 and rover.y == 3)


def test_move_south():
    rover = Rover("rover1", 1, 2, "S")
    rover.move()
    assert(rover.x == 1 and rover.y == 1)


def test_move_west():
    rover = Rover("rover1", 1, 2, "W")
    rover.move()
    assert(rover.x == 0 and rover.y == 2)


def test_move_east():
    rover = Rover("rover1", 1, 2, "E")
    rover.move()
    assert(rover.x == 2 and rover.y == 2)

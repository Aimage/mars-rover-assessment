from mars_rover.rover import Rover


def test_spin_left():
    rover = Rover("rover1", 1, 2, "N")
    rover.spin("L")
    assert(rover.direction == "W")


def test_spin_right():
    rover = Rover("rover1", 1, 2, "N")
    rover.spin("R")
    assert(rover.direction == "E")

from .rover import Rover


def command_rover(rover, command):
    for x in command:
        if x == "M":
            rover.move()
        else:
            rover.spin(x)


def initate_rover(name, init_position):
    init_position = init_position.split(" ")
    rover = Rover(name, int(init_position[0]), int(init_position[1]), init_position[2])
    return rover


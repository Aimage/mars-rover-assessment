import sys
from mars_rover.instruction import command_rover, initate_rover
from file_utils import read_instruction_from_file


def get_rover_from_input(rover_number):
    name = f"Rover{rover_number}"
    rover_landing = input(f"{name} Landing:")
    rover_instruction = input(f"{name} Instructions:")
    return name, rover_landing, rover_instruction


def run_from_keyboard_input():
    plateau = input("Plateau:")
    rover_number = 1
    while True:
        name, rover_landing, rover_instruction = get_rover_from_input(rover_number)
        rover = initate_rover(name, rover_landing)
        command_rover(rover, rover_instruction)
        print(rover)
        print("\n")
        rover_number += rover_number


def run_from_file_input(file_name):
    plateau, rover_landing_insctructions = read_instruction_from_file(file_name)
    for name in rover_landing_insctructions:
        rover = initate_rover(name, rover_landing_insctructions[name]["landing"])
        command_rover(rover, rover_landing_insctructions[name]["instruction"])
        print(rover)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        run_from_file_input(file_name)
    else:
        run_from_keyboard_input()

from marsrover.core.rover import Rover
from marsrover.models.coordinates import Coordinates
from marsrover.models.direction_movements import Directions
from marsrover.utils.command_parser import Parser


def get_direction_obj(direction: str):
    if direction.upper() == "N":
        dir_obj = Directions.N
    elif direction.upper() == "W":
        dir_obj = Directions.W
    elif direction.upper() == "E":
        dir_obj = Directions.E
    else:
        dir_obj = Directions.S
    return dir_obj


class Runner:

    def __init__(self):
        self.parser = Parser()

    def parse_file(self, file_path: str):
        with open(file_path, 'r') as input_file:
            input_line = input_file.readline()
            plateau = self.parser.parse_plateau_input(input_line)

            for lineCount, line in enumerate(input_file, 1):
                if lineCount % 2 != 0:
                    rover_initial_position = self.parser.parse_initial_position(line)
                else:
                    coordinates = Coordinates(int(rover_initial_position[0]), int(rover_initial_position[1]))
                    direction = get_direction_obj(rover_initial_position[2])
                    rover = Rover(plateau=plateau, coordinates=coordinates, direction=direction)
                    command = self.parser.parse_movement_commands(line)
                    rover.run(command)
                    print("rover initial position: {}".format(rover_initial_position))
                    print("input set of commands: {}".format(command))
                    print("final position: {}".format(rover.current_location()))


if __name__ == "__main__":
    Runner().parse_file("input_file.txt")

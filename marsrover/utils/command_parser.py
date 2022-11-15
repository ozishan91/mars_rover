import re
from typing import List

from marsrover.models.movement_commands import MovementCommands
from marsrover.models.plateau import Plateau
from marsrover.utils.custom_exceptions import ParsingError


class Parser:

    valid_plateau_input = re.compile("^[0-9]* [0-9]*$")
    valid_rover_position = re.compile("^[0-9]* [0-9]* [NSEW]$")

    def parse_initial_position(self, line: str) -> List[str]:
        if not re.match(self.valid_rover_position, line):
            raise ParsingError("Invalid rover initial position")
        return line.split()

    def parse_plateau_input(self, input_string: str) -> Plateau:
        if not re.match(self.valid_plateau_input, input_string):
            raise ParsingError("Invalid plateau dimensions")
        input_string_list = input_string.split()
        return Plateau(int(input_string_list[0]), int(input_string_list[1]))

    def parse_movement_commands(self, line: str) -> List[MovementCommands]:
        commands_list = [MovementCommands(command) for command in list(line.replace('\n', ''))]
        return commands_list

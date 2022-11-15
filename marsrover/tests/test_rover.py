from unittest import TestCase

from marsrover.core.rover import Rover
from marsrover.models.coordinates import Coordinates
from marsrover.models.direction_movements import Directions
from marsrover.models.plateau import Plateau
from marsrover.utils.command_parser import Parser
from marsrover.utils.custom_exceptions import OutOfBoundException


class TestRover(TestCase):

    def setUp(self) -> None:
        self.parser = Parser()

    def test_turn_left(self):
        plateau = Plateau(5, 5)
        coordinates = Coordinates(1, 2)
        rover = Rover(plateau=plateau, coordinates=coordinates, direction=Directions.N)
        rover.turn_left()
        actual_output = rover.current_location()
        expected_output = "1 2 W"
        self.assertEqual(expected_output, actual_output)

    def test_turn_right(self):
        plateau = Plateau(5, 5)
        coordinates = Coordinates(1, 2)
        rover = Rover(plateau=plateau, coordinates=coordinates, direction=Directions.N)
        rover.turn_right()
        actual_output = rover.current_location()
        expected_output = "1 2 E"
        self.assertEqual(expected_output, actual_output)

    def test_move_success(self):
        plateau = Plateau(5, 5)
        coordinates = Coordinates(1, 2)
        rover = Rover(plateau=plateau, coordinates=coordinates, direction=Directions.N)
        rover.move()
        actual_output = rover.current_location()
        expected_output = "1 3 N"
        self.assertEqual(expected_output, actual_output)

    def test_move_raise_exception(self):
        plateau = Plateau(3, 3)
        coordinates = Coordinates(1, 2)
        rover = Rover(plateau=plateau, coordinates=coordinates, direction=Directions.N)
        rover.move()
        with self.assertRaises(OutOfBoundException):
            rover.move()

    def test_run1(self):
        plateau = Plateau(5, 5)
        coordinates = Coordinates(1, 2)
        rover = Rover(plateau=plateau, coordinates=coordinates, direction=Directions.N)
        commands = "LMLMLMLMM"

        rover.run(self.parser.parse_movement_commands(commands))
        actual_output = rover.current_location()
        expected_output = "1 3 N"
        self.assertEqual(expected_output, actual_output)

    def test_run2(self):
        plateau = Plateau(5, 5)
        coordinates = Coordinates(3, 3)
        rover = Rover(plateau=plateau, coordinates=coordinates, direction=Directions.E)
        commands = "MMRMMRMRRM"
        rover.run(self.parser.parse_movement_commands(commands))
        actual_output = rover.current_location()
        expected_output = "5 1 E"
        self.assertEqual(expected_output, actual_output)

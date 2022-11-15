import logging

from marsrover.core.command_factory import CommandFactory
from marsrover.models.coordinates import Coordinates
from marsrover.models.plateau import Plateau
from marsrover.utils.custom_exceptions import OutOfBoundException, ApplicationExecutionException


class Rover:

    def __init__(self, plateau: Plateau, coordinates: Coordinates, direction):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.plateau = plateau
        self.coordinates = coordinates
        self.direction = direction

    def turn_left(self):
        self.direction = self.direction.turn_left

    def turn_right(self):
        self.direction = self.direction.turn_right

    def move(self):
        new_coordinates = self.coordinates.get_new_coordinates(
            self.direction.next_step_on_x_axis, self.direction.next_step_on_y_axis
        )
        if self.plateau.is_next_step_valid(new_coordinates):
            self.logger.info("New coordinates are valid {}, {}".format(
                new_coordinates.x_coordinate, new_coordinates.y_coordinate)
            )
            self.coordinates = new_coordinates
        else:
            raise OutOfBoundException("The command is not valid as it is breaching the boundaries of the plateau")

    def current_location(self):
        return str(self.coordinates.x_coordinate) + " " + str(self.coordinates.y_coordinate) + " " + \
               self.direction.current_direction

    def run(self, command_list):
        command_factory = CommandFactory()
        try:
            for command in command_list:
                self.logger.info("before {}".format(self.current_location()))
                runner = command_factory.get_command_runner(command)
                runner.execute(self)
                self.logger.info("after {}".format(self.current_location()))
        except ApplicationExecutionException as e:
            self.logger.error(e.__traceback__)
            self.logger.error(e)

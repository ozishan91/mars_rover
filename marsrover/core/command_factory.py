from marsrover.models.movement_commands import MovementCommands


class LeftCommand:

    def execute(self, rover):
        rover.turn_left()


class RightCommand:

    def execute(self, rover):
        rover.turn_right()


class MoveCommand:

    def execute(self, rover):
        rover.move()


class CommandFactory:

    def __init__(self):
        self.command_map = {
            MovementCommands.LEFT: LeftCommand(),
            MovementCommands.RIGHT: RightCommand(),
            MovementCommands.MOVE: MoveCommand()
        }

    def get_command_runner(self, command: MovementCommands):
        return self.command_map.get(command)

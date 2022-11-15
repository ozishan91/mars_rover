
class Coordinates:

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def get_new_coordinates(self, x_step_value, y_step_value):
        return Coordinates(self.x_coordinate + x_step_value, self.y_coordinate + y_step_value)

    def is_within_upper_bound(self, new_coordinates):
        return self.x_coordinate >= new_coordinates.x_coordinate and self.y_coordinate >= new_coordinates.y_coordinate

    def is_within_lower_bound(self, new_coordinates):
        return self.x_coordinate <= new_coordinates.x_coordinate and self.y_coordinate <= new_coordinates.y_coordinate



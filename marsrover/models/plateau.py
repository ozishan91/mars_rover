from marsrover.models.coordinates import Coordinates


class Plateau:

    def __init__(self, top_right_x_coordinate, top_right_y_coordinate):
        self.top_right_coordinate = Coordinates(top_right_x_coordinate, top_right_y_coordinate)
        self.bottom_left_coordinate = Coordinates(0, 0)

    def is_next_step_valid(self, new_coordinates):
        return self.top_right_coordinate.is_within_upper_bound(new_coordinates) \
               and self.bottom_left_coordinate.is_within_lower_bound(new_coordinates)

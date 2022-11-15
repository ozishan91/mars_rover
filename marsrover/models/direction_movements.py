
class Movements:

    def __init__(self, current_direction, next_step_on_x_axis, next_step_on_y_axis):
        self.current_direction = current_direction
        self.next_step_on_x_axis = next_step_on_x_axis
        self.next_step_on_y_axis = next_step_on_y_axis
        self.turn_right = None
        self.turn_left = None

    def set_turn_left(self, left_movement):
        self.turn_left = left_movement
        return self

    def set_turn_right(self, right_movement):
        self.turn_right = right_movement
        return self


class Directions:
    N = Movements("N", 0, 1)
    S = Movements("S", 0, -1)
    W = Movements("W", -1, 0)
    E = Movements("E", 1, 0)

    N.set_turn_right(E).set_turn_left(W)
    S.set_turn_right(W).set_turn_left(E)
    W.set_turn_right(N).set_turn_left(S)
    E.set_turn_right(S).set_turn_left(N)

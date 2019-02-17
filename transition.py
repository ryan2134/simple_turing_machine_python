from state import State


# Contains the current and next state as well as the current and next char to write to the tape
class Transition:
    def __init__(self, current_state, current_char, new_state, new_char, direction):
        self.current_state = current_state
        self.current_char = current_char
        self.new_state = new_state
        self.new_char = new_char
        self.direction = direction

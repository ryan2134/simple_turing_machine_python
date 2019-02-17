from state import StateType


class TuringMachine:
    def __init__(self, states, transitions, tape):
        self.states = states
        self.start_state = self.get_start_state()
        self.transitions = transitions
        self.tape = tape

    # Returns the tape state of the turing machine 
    def get_tape(self):
        return self.tape.get_tape()

    # Gets the start state of the given word
    def get_start_state(self):
        return next(state for state in self.states if state.type == StateType.Start)

    # Handles the processing of this simple turing machine
    def process(self, verbose=False):
        current_state = self.start_state

        # keep iterating until we get to the final state type
        while current_state.type != StateType.Final:
            current_char = self.tape.read()
            state_id = current_state.id

            # First obtain the transition and its information
            transition = next(t for t in self.transitions
                              if t.current_state == state_id
                              and t.current_char == current_char)

            # Change the current state from the given transition
            current_state = next(state for state in self.states if state.id == transition.new_state)

            # Given the info, write and move tape head
            self.tape.write(transition.new_char)
            self.tape.move_head(transition.direction)

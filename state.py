from enum import Enum


# Represents the current state of the tape in simulation
class StateType(Enum):
    Start = 1
    Final = 2
    Empty = 3


# Id which will later be evaluated by the turing-machine
class State:
    def __init__(self, id, state_type):
        self.id = id
        self.type = state_type

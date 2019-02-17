from turing_machine import TuringMachine
from state import State, StateType
from transition import Transition
from direction import Direction
from tape import Tape


# Simple test to check whether the turing machine is working
tape = Tape('|||', '|')
states = [
    State("s0", StateType.Start),
    State("s1", StateType.Empty),
    State("sf", StateType.Final)
]

transitions = [
    Transition("s0", "$", "s1", "$", Direction.Right),
    Transition("s1", "|", "s1", "|", Direction.Right),
    Transition("s1", "#", "sf", "|", Direction.Neutral)
]

tm = TuringMachine(states, transitions, tape)
tm.process()
print(tm.get_tape())

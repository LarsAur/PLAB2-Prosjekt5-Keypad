'''The rule navigation class'''
from inspect import isfunction

def signal_is_digit(signal):
    '''Validates that signal is an integer 0 - 9'''
    return 48 <= ord(signal) <= 57


def all_symbols(signal):
    '''Acknowledges that all input is signal'''
    return True

class Rule:
    """The rule class"""

    def __init__(self, state1, state2, signal, action):
        self.state1 = state1
        self.state2 = state2
        self.signal = signal
        self.action = action

    def match(self, state, symbol):
        """Checks if correct state, and execute operation"""
        if state == self.state1:
            if isfunction(self.signal):
                return self.signal(symbol)
            else:
                return symbol == self.signal
        return False

def signal_is_digit(signal):
    return 48 <= ord(signal) <= 57

def all_symbols(signal):
    return True

from inspect import isfunction

class Rule:

    def __init__(self, state_1, state_2, signal, action):
        self.state1 = state_1
        self.state2 = state_2
        self.signal = signal
        self.action = action

    def match(self, state, symbol):
        if state == self.state1:
            if isfunction(self.signal):
                return self.signal(str(symbol))
            else:
                return symbol == self.signal
        return False

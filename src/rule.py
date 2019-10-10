class Rule:

  def __init__(self, state_1, state_2, signal, action):
    self.state1 = state_1
    self.state2 = state_2
    self.signal = signal
    self.action = action
    self.symbol = None

  def match(self, state, symbol):
    if state == self.state_1 and symbol == self.signal:
      return True
    return False
    
    

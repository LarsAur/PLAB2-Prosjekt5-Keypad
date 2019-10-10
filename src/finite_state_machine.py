class FSM:

  def __init__(self, agent):
    self.rule_list = []
    self.state = "S-Init"
    self.signal = None
    self.agent = agent


  def add_rule(self, rule):
    self.rule_list.append(rule)


  def get_next_signal(self):
    pass 
  
  def run_rules(self):
    pass

  def apply_rule(self):
    pass

  def fire_rule(self):
    pass

  def main_loop(self):
    pass

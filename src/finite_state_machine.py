class FSM:

    def __init__(self, agent):
        self.rule_list = []
        self.state = "S-Init"
        self.signal = None
        self.agent = agent

    def add_rule(self, rule):
        """Adding a rule to the fsm"""
        self.rule_list.append(rule)

    def get_next_signal(self):
        """Query the agent for the next signal."""
        self.agent.get_next_signal()

    def run_rules(self):
        for rule in self.rule_list:
            if self.apply_rule(rule):
                self.fire_rule(rule)

    def apply_rule(self, rule):
        """Returns if the rule matches the current state and signal"""
        return rule.match(self.state, self.signal)

    def fire_rule(self, rule):
        """Sets the new state of the fsm and fires the method from rule"""
        self.state = rule.state2
        rule.action(self.agent, self.signal)

    def main_loop(self):
        """Sets the current stat to init-state and runs the fsm in a loop, asking for input"""
        self.state = "S-Init"
        # TODO end on final state
        while True:
            self.signal = self.agent.get_next_signal()
            self.run_rules()

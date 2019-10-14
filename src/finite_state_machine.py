"""The finite state machine class"""
from inspect import signature

class FSM:
    """The finite state machine class"""

    def __init__(self, agent):
        self.state = "S-Init"
        self.signal = None
        self.agent = agent
        self.rule_list = self.agent.init_rules  # gets init rules from agent

    def add_rule(self, rule):
        """Adding a rule to the fsm"""
        self.rule_list.append(rule)

    def get_next_signal(self):
        """Query the agent for the next signal."""
        self.agent.get_next_signal()

    def run_rules(self):
        """Runs through the rules"""
        for rule in self.rule_list:
            if self.apply_rule(rule):
                self.fire_rule(rule)
                return

    def apply_rule(self, rule):
        """Returns if the rule matches the current state and signal"""
        return rule.match(self.state, self.signal)

    def fire_rule(self, rule):
        """Sets the new state of the fsm and fires the method from rule"""
        self.state = rule.state2
        sig = signature(rule.action)

        if len(sig.parameters) == 1 and not self.signal is None:
            rule.action(self.signal)
        else:
            rule.action()

    def main_loop(self):
        """Sets the current stat to init-state and runs the fsm in a loop, asking for input"""
        while True:
            self.signal = self.agent.get_next_signal()
            self.run_rules()

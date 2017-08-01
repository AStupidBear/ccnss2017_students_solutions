class Node(object):
    def __init__(self, parent):
        self.parent = parent
        self.children = {}
        self.q = 0
        self.n = 0


class ActionNode(Node):
    """
    A node holding an action in the tree.
    """
    def __init__(self, parent, action):
        super(ActionNode, self).__init__(parent)
        self.action = action
        self.n = 0

    def sample_state(self, real_world=False):  
        state = self.parent.state.perform(self.action)

        if state not in self.children:
            self.children[state] = StateNode(self, state)

        return self.children[state]

    def __str__(self):
        return "Action: {}".format(self.action)


class StateNode(Node):
    """
    A node holding a state in the tree.
    """
    def __init__(self, parent, state):
        super(StateNode, self).__init__(parent)
        self.state = state
        self.reward = 0
        for action in state.actions:
            self.children[action] = ActionNode(self, action)

    @property
    def untried_actions(self):
        """
        All actions which have never be performed
        :return: A list of the untried actions.
        """
        return [a for a in self.children if self.children[a].n == 0]

    @untried_actions.setter
    def untried_actions(self, value):
        raise ValueError("Untried actions can not be set.")

    def __str__(self):
        return "State: {}".format(self.state)

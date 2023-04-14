from .basic import Composite, Status

class Sequence(Composite):
    """
    The Sequence node is a subclass of Composite that represents a sequence of child 
    nodes in a behavior tree. The Sequence node executes its child nodes in order, from 
    left to right, until one of the child nodes fails or all of them succeed. 

    By using the Sequence node in a behavior tree, we can ensure that a sequence of tasks 
    are executed in order, and that the behavior tree moves on to the next task only if 
    the previous task succeeds. If any task fails, the Sequence node returns FAILURE and 
    stops executing the sequence. The Sequence node is a fundamental building block for 
    constructing complex behavior trees, and can be used in conjunction with other types 
    of nodes to implement more sophisticated behaviors.

    Properties:
    current_child: A reference to the current child node being executed. This is None if no 
    child nodes are currently being executed.

    Methods:
    tick(): Executes a single tick of the behavior tree starting from the current node.
    """
    def __init__(self, children):
        super().__init__()
        self.children = children
        for child in self.children:
            child.parent = self
        self.current_child = None

    def tick(self):
        print("Sequence: {}".format(self.children))
        for self.current_child in self.children:
            status = self.current_child.tick()
            if status != Status.SUCCESS:
                return status
        return Status.SUCCESS
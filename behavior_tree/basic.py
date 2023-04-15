from enum import Enum
from .blackboard import Blackboard

class Status(Enum):
    SUCCESS = 0
    FAILURE = 1
    RUNNING = 2

class Node:
    """
    The Node class provides the basic functionality needed for constructing a behavior 
    tree, such as maintaining the parent-child relationships between nodes and tracking 
    the status of each node. Subclasses of Node can add additional functionality by 
    implementing the tick() and reset() methods, which define the behavior of the node. 
    By subclassing Node and implementing these methods, we can create custom nodes 
    that perform specific tasks in our behavior tree.

    Properties:
    parent: A reference to the parent node of the current node. This is None if the 
    node has no parent.
    children: A list of the child nodes of the current node. This is an empty list if 
    the node has no children.
    status: The current status of the node, which is an instance of the Status 
    enumeration (SUCCESS, FAILURE, or RUNNING).

    Methods:
    tick(): Executes a single tick of the behavior tree starting from the current 
    node. This method must be implemented by subclasses of Node and should return the 
    current status of the node after the tick has been executed.
    reset(): Resets the state of the node to its initial state. This method can be 
    implemented by subclasses of Node if they have any state that needs to be reset.
    """
    def __init__(self, blackboard=None):
        self.parent = None
        self.children = []
        self.blackboard = blackboard
        self.status = None

    def __repr__(self):
        return self.__class__.__name__

    def tick(self):
        raise NotImplementedError
    
    def reset(self):
        pass

class Action(Node):
    """
    The Action class is a subclass of Node that represents the leaf nodes in the behavior 
    tree, which are nodes that cannot have any child nodes.
    """
    pass

class Composite(Node):
    """
    The Composite class is a subclass of Node that represents the composite nodes in a 
    behavior tree, which are nodes that can have one or more child nodes.

    Properties:
    children: A list of the child nodes of the current node. This is an empty list if the 
    node has no children.

    Methods:
    add_child(child): Adds a child node to the current node. The child node should be an 
    instance of a subclass of Node.
    remove_child(child): Removes a child node from the current node. The child node should 
    be an instance of a subclass of Node.
    reset(): Resets the state of the node to its initial state, including resetting the 
    state of all child nodes.
    """
    def __init__(self):
        super().__init__()
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def remove_child(self, child):
        self.children.remove(child)
        child.parent = None

    def reset(self):
        super().reset()
        for child in self.children:
            child.reset()

class Decorator(Node):
    """
    The Decorator class is a subclass of Node that represents a decorator node in a 
    behavior tree. Decorator nodes modify the behavior of their child nodes in some way,
    without changing the outcome of the behavior tree.

    The Decorator class is a base class for several types of decorator nodes in a behavior 
    tree, such as the Inverter, Succeeder, and Repeater nodes. These nodes modify the 
    behavior of their child nodes in different ways, such as inverting their outcome, 
    always succeeding or failing, or repeating their behavior multiple times.

    By providing a common interface for decorator nodes, the Decorator class allows us to 
    easily create new decorator nodes and reuse existing ones, making it easier to construct 
    complex behavior trees.
    """
    def __init__(self, child):
        super().__init__()
        self.children.append(child)
        child.parent = self

    @property
    def child(self):
        return self.children[0]
    
    def reset(self):
        super().reset()
        self.child.reset()
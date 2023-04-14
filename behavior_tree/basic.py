from enum import Enum

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
    def __init__(self):
        self.parent = None
        self.children = []
        self.status = None

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
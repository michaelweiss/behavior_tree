class Blackboard:
    """
    A blackboard allows nodes to share data with each other.

    While currently the blackboard is implemented as a dictionary, this is an implementation
    detail that may change in the future. Possible extensions may include a more sophisticated
    data structure, eg one that include parameters. Nodes should not access the blackboard 
    data directly, but should use the get() and set() methods instead.

    Properties:
    data: A dictionary that stores the data shared between nodes.
    
    Methods:
    get(key): Returns the value associated with the given key.
    set(key, value): Sets the value associated with the given key.
    """
    def __init__(self):
        self.data = {}

    def get(self, key):
        if key not in self.data:
            return None
        return self.data[key]

    def set(self, key, value):
        self.data[key] = value
class Blackboard:
    """
    A blackboard allows nodes to share data between each other.

    Properties:
    data: A dictionary that stores the data shared between nodes.
    
    Methods:
    get(key): Returns the value associated with the given key.
    set(key, value): Sets the value associated with the given key.
    """
    def __init__(self):
        self.data = {}

    def get(self, key):
        return self.data[key]

    def set(self, key, value):
        self.data[key] = value
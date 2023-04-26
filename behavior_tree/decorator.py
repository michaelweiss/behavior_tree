from .basic import Decorator, Status
            
class Inverter(Decorator):
    """
    A subclass of Decorator that inverts the status of its child node. If the child node succeeds, 
    the Inverter node returns FAILURE. If the child node fails, the Inverter node returns SUCCESS.
    """
    def tick(self):
        status = self.child.tick()
        if status == Status.SUCCESS:
            return Status.FAILURE
        elif status == Status.FAILURE:
            return Status.SUCCESS
        return status
    
class Succeeder(Decorator):
    """
    A subclass of Decorator that always succeeds, regardless of the status of its child node. 
    """
    def tick(self):
        self.child.tick()
        return Status.SUCCESS
    
class Failer(Decorator):
    """
    A subclass of Decorator that always fails, regardless of the status of its child node. 
    """
    def tick(self):
        self.child.tick()
        return Status.FAILURE
    
class RepeatUntilSuccess(Decorator):
    """
    A subclass of Decorator that repeats its child node until the child node succeeds. Once the 
    child node succeeds, the RepeatUntilSuccess node succeeds.
    """
    def tick(self):
        while True:
            status = self.child.tick()
            if status == Status.SUCCESS:
                return Status.SUCCESS
            
class RepeatUntilFailure(Decorator): 
    """
    A subclass of Decorator that repeats its child node until the child node fails. Once the child 
    node fails, the RepeatUntilFailure node succeeds.
    """
    def tick(self):
        while True:
            status = self.child.tick()
            if status == Status.FAILURE:
                return Status.SUCCESS

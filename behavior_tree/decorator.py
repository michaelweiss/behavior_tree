from .basic import Decorator, Status

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

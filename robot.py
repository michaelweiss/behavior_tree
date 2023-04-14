from behavior_tree.basic import Action, Status
from behavior_tree.control import Sequence

class Robot:
    def __init__(self):
        self.behavior = Sequence([
            GoToTarget(),
            PickUpTarget(),
            GoToBase(),
            DropTarget()
        ])

    def run(self):
        self.behavior.tick()

class GoToTarget(Action):
    def tick(self):
        print("Going to target")
        return Status.SUCCESS
    
class PickUpTarget(Action):
    def tick(self):
        print("Picking up target")
        return Status.SUCCESS
    
class GoToBase(Action):
    def tick(self):
        print("Going to base")
        return Status.SUCCESS
    
class DropTarget(Action):
    def tick(self):
        print("Dropping target")
        return Status.SUCCESS
    
if __name__ == "__main__":
    robot = Robot()
    robot.run()
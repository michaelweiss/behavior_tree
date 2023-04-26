from behavior_tree.basic import Action, Status
from behavior_tree.control import Sequence

"""
This is simple test of the behavior tree. The robot will go to the target, pick it up, 
go to the base, and drop it. The robot will perform these actions in order.
"""

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
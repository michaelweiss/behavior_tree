from behavior_tree.basic import *

class Robot:
    def __init__(self):
        # self.behavior = Sequence(
        #     [GoToTarget(),
        #      PickUpTarget(),
        #      GoToBase(),
        #      DropTarget()
        #     ])
        self.behavior = GoToTarget()

    def run(self):
        self.behavior.tick()

class GoToTarget(Action):
    def tick(self):
        print("Going to target")
        return Status.SUCCESS
    
if __name__ == "__main__":
    robot = Robot()
    robot.run()
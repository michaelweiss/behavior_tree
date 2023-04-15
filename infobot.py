from behavior_tree.basic import Action, Status
from behavior_tree.control import Sequence
from behavior_tree.blackboard import Blackboard

class Infobot:
    def __init__(self):
        self.blackboard = Blackboard()
        self.behavior = Sequence([
            ReadSentence(self.blackboard),
            LowercaseSentence(self.blackboard),
            TokenizeSentence(self.blackboard)
        ])

    def run(self):
        self.behavior.tick()
        print("Tokens: {}".format(self.blackboard.get("tokens")))

class ReadSentence(Action):
    def tick(self):
        print("Reading sentence")
        sentence = input("Enter a sentence: ")
        self.blackboard.set("sentence", sentence)
        return Status.SUCCESS
    
class LowercaseSentence(Action):
    def tick(self):
        print("Lowercase sentence")
        sentence = self.blackboard.get("sentence")
        lowercased = sentence.lower()
        self.blackboard.set("sentence", lowercased)
        return Status.SUCCESS
    
class TokenizeSentence(Action):
    def tick(self):
        print("Tokenizing sentence")
        sentence = self.blackboard.get("sentence")
        tokens = sentence.split()
        self.blackboard.set("tokens", tokens)
        return Status.SUCCESS
    
if __name__ == "__main__":
    infobot = Infobot()
    infobot.run()
from behavior_tree.basic import Action, Decorator, Status
from behavior_tree.control import Sequence
from behavior_tree.decorator import RepeatUntilFailure
from behavior_tree.blackboard import Blackboard

class Infobot:
    def __init__(self):
        self.blackboard = Blackboard()
        self.behavior = Sequence([
            ReadSentence(self.blackboard),
            LowercaseSentence(self.blackboard),
            TokenizeSentence(self.blackboard),
            RepeatUntilFailure(
                ProcessToken(self.blackboard))
        ])

    def run(self):
        self.behavior.tick()
        print("Tokens: {}".format(self.blackboard.get("tokens")))

class ReadSentence(Action):
    def tick(self):
        print("Reading sentence")
        sentence = input("Enter a sentence: ").strip()
        self.blackboard.set("sentence", sentence)
        return Status.SUCCESS
    
class LowercaseSentence(Action):
    def tick(self):
        print("Lowercase sentence")
        sentence = self.blackboard.get("sentence")
        if not sentence:
            print("No sentence to lowercase")
            return Status.FAILURE
        lowercased = sentence.lower()
        self.blackboard.set("sentence", lowercased)
        return Status.SUCCESS
    
class TokenizeSentence(Action):
    def tick(self):
        print("Tokenizing sentence")
        sentence = self.blackboard.get("sentence")
        if not sentence:
            print("No sentence to tokenize")
            return Status.FAILURE
        tokens = sentence.split()
        self.blackboard.set("tokens", tokens)
        return Status.SUCCESS
    
class ProcessToken(Action):
    def tick(self):
        print("Processing token")
        tokens = self.blackboard.get("tokens")
        if not tokens:
            print("No more tokens to process")
            return Status.FAILURE
        token = tokens.pop(0)
        print("Token: {}".format(token))
        self.blackboard.set("tokens", tokens)
        return Status.SUCCESS
    
if __name__ == "__main__":
    infobot = Infobot()
    infobot.run()
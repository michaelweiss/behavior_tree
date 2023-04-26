from behavior_tree.basic import Action, Decorator, Status
from behavior_tree.control import Sequence, Selector
from behavior_tree.decorator import RepeatUntilFailure, Inverter,  Failer
from behavior_tree.blackboard import Blackboard

"""
In this example, we use a behavior tree to process a sentence. The infobot will read a 
sentence, lowercase it, tokenize it, and then process each token.

This example also demonstrates the use of the blackboard. A blackboard class is a simple 
dictionary that can be used to share data between actions. In this example, the sentence is
stored in the blackboard and then retrieved by each action that needs it. The tokens are
also stored in the blackboard and retrieved by the ProcessToken action.
"""

class Infobot:
    def __init__(self):
        self.blackboard = Blackboard()
        self.behavior = Sequence([
            # To test the selector, we check if the sentence is empty. If it is, we use the
            # default sentence. If it isn't, we use the sentence entered by the user.
            Selector([
                ReadSentence(self.blackboard),
                UseDefaultSentence(self.blackboard)
            ]),
            # To test the inverter, we check wrap the LowercaseSentence action in a failer.
            Inverter(
                Failer(LowercaseSentence(self.blackboard))),
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
        if not sentence:
            print("No sentence entered")
            return Status.FAILURE
        self.blackboard.set("sentence", sentence)
        return Status.SUCCESS
    
class UseDefaultSentence(Action):
    def tick(self):
        print("Using default sentence")
        self.blackboard.set("sentence", "The quick brown Fox jumps over the lazy Dog.")
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
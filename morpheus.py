import random

class MorpheusWisdom:
    """
    Morpheus - The guide who offers the choice between truth and comfortable illusion
    "This is your last chance. After this, there is no going back."
    """
    
    def __init__(self):
        self.pills_offered = 0
        self.wisdom_dispensed = 0
    
    def offer_choice(self):
        """
        Offer the choice between the red pill and blue pill.
        The fundamental choice between truth and illusion.
        """
        choice_text = """
        This is your last chance. After this, there is no going back.
        
        You take the blue pill—the story ends, you wake up in your bed 
        and believe whatever you want to believe.
        
        You take the red pill—you stay in Wonderland, and I show you 
        how deep the rabbit hole goes.
        
        Remember: all I'm offering is the truth. Nothing more.
        """
        self.pills_offered += 1
        return choice_text
    
    def explain_reality(self):
        """
        Explain the nature of the Matrix to the newly awakened.
        The real world is harsh, but it is real.
        """
        explanation = """
        The Matrix is a system, Neo. That system is our enemy. 
        But when you're inside, you look around, what do you see? 
        Businessmen, teachers, lawyers, carpenters. 
        The very minds of the people we are trying to save.
        
        But until we do, these people are still a part of that system 
        and that makes them our enemy.
        """
        self.wisdom_dispensed += 1
        return explanation
    
    def training_wisdom(self):
        """
        Provide training wisdom for those learning to navigate reality.
        Your mind makes it real.
        """
        wisdoms = [
            "There is no spoon.",
            "Do not try and bend the spoon. That's impossible.",
            "Instead, only try to realize the truth: there is no spoon.",
            "Your mind makes it real.",
            "Free your mind.",
            "Belief. It's the one thing that defines the impossible."
        ]
        return random.choice(wisdoms)
    
    def final_lesson(self):
        """
        The most important lesson: believing in yourself.
        There is a difference between knowing the path and walking the path.
        """
        return "There is a difference between knowing the path and walking the path."

def main():
    morpheus = MorpheusWisdom()
    print("Morpheus speaks:")
    print(morpheus.offer_choice())
    print("\nWisdom for the journey:")
    print(morpheus.training_wisdom())
    
if __name__ == "__main__":
    main()

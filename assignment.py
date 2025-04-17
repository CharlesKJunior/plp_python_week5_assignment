## This is my assignment1.py
# Assignment 1: This is my Own Class
# Here we model a Superhero with inheritance to explore OOP concepts

class Superhero:
    def __init__(self, name, superpower, health=100, energy=100):
        """
        Initialize a Superhero with:
        - name: hero's identity
        - superpower: description of ability
        - health: starts at 100
        - energy: starts at 100
        """
        self.name = name
        self.superpower = superpower
        self.health = health
        self.energy = energy

    def use_power(self):
        """
        Hero uses their superpower, which costs energy.
        """
        if self.energy >= 20:
            self.energy -= 20
            print(f"{self.name} uses {self.superpower}! 💥")
        else:
            print(f"{self.name} is too tired to use their power.")

    def rest(self):
        """
        Restore energy by resting.
        """
        self.energy = min(self.energy + 30, 100)
        self.health = min(self.health + 10, 100)
        print(f"{self.name} rests and recovers strength. 🌟")

    def get_status(self):
        """
        Print current health and energy.
        """
        print(f"Status of {self.name} -> Health: {self.health}/100, Energy: {self.energy}/100")

# Here Inheritance layer: a Sidekick inherits from Superhero
class Sidekick(Superhero):
    def __init__(self, name, superpower, mentor):
        super().__init__(name, superpower)
        self.mentor = mentor  
    def assist(self):
        """
        Sidekick assists their mentor, boosting mentor's energy.
        """
        if self.energy >= 10:
            self.energy -= 10
            self.mentor.energy = min(self.mentor.energy + 10, 100)
            print(f"{self.name} assists {self.mentor.name}! 🤝")
        else:
            print(f"{self.name} needs to rest before assisting.")

# Demonstration
if __name__ == "__main__":
    hero = Superhero("Aurora", "Light Beam")
    sidekick = Sidekick("Spark", "Electric Spark", hero)

    hero.get_status()
    hero.use_power()
    hero.get_status()

    sidekick.get_status()
    sidekick.assist()
    sidekick.get_status()
    hero.get_status()

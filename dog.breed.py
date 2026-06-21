class Dog:
    """Dog class demonstrating class and instance variables."""

    animal = "Dog"

    def __init__(self, breed, color):
        """Constructor to intialize instance variables."""

        self.breed = breed
        self.color = color
          
    def display_details(self):
        """Display dog details."""
        print(f"Animal: {self.animal}")
        print(f"Breed: {self.breed}")
        print(f"Color: {self.color}")
        print("-" * 30)

dog1 = Dog("German Shepherd", "Black and Tan")
dog2 = Dog("Golden Retriever", "Golden")

print("=" * 30)
print("DOG DETAILS")
print("=" * 30)

print("\nDog 1:")
dog1.display_details()

print("\nDog 2:")
dog2.display_details()

print("\n" + "=" * 30)
print("DEMONSTRATING CLASS VS INSTANCE VARIABLES")
print("=" * 30)

print(f"\nClass variable 'animal': {Dog.animal}")
print(f"Dog 1 'animal': {dog1.animal}")
print(f"Dog 2 'animal': {dog2.animal}")
Dog.animal = "Canine"
print(f"\nAfter changing class variable to 'Canine': ")
print(f"Dog 1: {dog1.animal}")
print(f"Dog 2: {dog2.animal}")

dog1.breed = "Labrador"
print(f"\nAfter changing Dog 1's breed to 'Labrador':")
print(f"Dog 1 'breed': {dog1.breed}")
print(f"Dog 2 'breed': {dog2.breed}")
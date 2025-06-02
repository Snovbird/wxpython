class Dog:
    # Class variable shared by all instances
    species = "Canis familiaris"
    
    # Initializer / Constructor
    def __init__(myself, name, age):
        # Instance variables unique to each instance
        myself.name = name
        myself.age = age
    
    # Instance method
    def bark(myself):
        return f"{myself.name} says Woof!"
    
    # Another instance method
    def get_info(myself):
        return f"{myself.name} is {myself.age} years old."

# Create two Dog instances
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

# Access attributes
print(buddy.name)  # Output: "Buddy"
print(miles.age)   # Output: 4

# Call methods
print(buddy.bark())  # Output: "Buddy says Woof!"
print(miles.get_info())  # Output: "Miles is 4 years old."

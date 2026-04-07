"""
from faker import Faker
import random

fake = Faker()

# Function to generate a random quest
def quest():
    actions = ["retrieve", "protect", "deliver", "investigate", "defeat"]
    objects = ["artifact", "message", "treasure", "weapon", "secret"]
    places = ["ancient ruins", "haunted forest", "lost city", "dungeon", "kingdom"]
    
    return f"Your quest is to {random.choice(actions)} a {random.choice(objects)} from the {random.choice(places)}."

# Function to generate a random backstory
def backstory():
    return f"{fake.name()} was born in {fake.city()} and once worked as a {fake.job()}. After a mysterious event, they now seek adventure."

# Function to generate a random name
def name():
    return fake.name()

# Example usage
print("Name:", name())
print("Backstory:", backstory())"""
print("Quest:", quest())

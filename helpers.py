from faker import Faker

fake = Faker()

def quest():
    return fake.sentence()

def backstory():
    return fake.text()

def name():
    return fake.name()
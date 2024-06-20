import random

def generate_random_animal():
    animals = ['dog', 'cat', 'bird', 'elephant', 'lion', 'tiger', 'snake', 'rabbit']
    return random.choice(animals)

if __name__ == "__main__":
    random_animal = generate_random_animal()
    print(random_animal)
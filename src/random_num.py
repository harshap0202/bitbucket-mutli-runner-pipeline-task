import random

def generate_random_num():
    return ''.join(random.choices('0123456789', k=10))

if __name__ == "__main__":
    random_num = generate_random_num()
    print(random_num)
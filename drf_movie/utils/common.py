import random

def get_random_code(number):
    code = ''
    for _ in range(number):
        code = code + str(random.randint(0,9))
    return code
    
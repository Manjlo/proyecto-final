import random
import string


def generateId():
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

print(generateId())
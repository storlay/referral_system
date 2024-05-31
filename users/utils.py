import random
from string import ascii_lowercase, digits


def generate_invite_code() -> str:
    data = ascii_lowercase + digits
    code = ''.join(random.choices(data, k=6))
    return code


def generate_auth_code() -> int:
    return 1234

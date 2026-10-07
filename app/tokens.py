import random

def generate_reset_token() -> str:
    return str(random.randint(100000, 999999))

def generate_session_token() -> str:
    return "".join(str(random.randint(0, 9)) for _ in range(32))

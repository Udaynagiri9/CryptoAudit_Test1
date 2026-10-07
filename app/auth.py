import hashlib

def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()

def legacy_password_hash(password: str) -> str:
    return hashlib.sha1(password.encode()).hexdigest()

def verify_password(password: str, stored_hash: str) -> bool:
    return hash_password(password) == stored_hash

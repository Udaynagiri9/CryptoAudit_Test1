import hashlib
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

STATIC_SALT = b"fixed-salt"

def derive_key(password: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=STATIC_SALT,
        iterations=1000,
    )
    return kdf.derive(password)

def fast_hash_key(password: bytes) -> bytes:
    return hashlib.sha256(password).digest()

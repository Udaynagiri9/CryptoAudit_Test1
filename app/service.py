from app.auth import hash_password
from app.encryption import encrypt_record
from app.passwords import derive_key
from app.tokens import generate_reset_token

def create_user(password: str, secret: bytes) -> dict:
    return {
        "password_hash": hash_password(password),
        "encrypted_secret": encrypt_record(secret),
        "derived_key": derive_key(password.encode()),
        "reset_token": generate_reset_token(),
    }

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

KEY = b"0123456789abcdef0123456789abcdef"
STATIC_IV = b"123456789012"

def encrypt_message(message: bytes) -> bytes:
    cipher = Cipher(algorithms.AES(KEY), modes.GCM(STATIC_IV))
    encryptor = cipher.encryptor()
    return encryptor.update(message) + encryptor.finalize()

def decrypt_message(ciphertext: bytes) -> bytes:
    cipher = Cipher(algorithms.AES(KEY), modes.GCM(STATIC_IV))
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()

from Crypto.Cipher import AES

KEY = b"0123456789abcdef"

def encrypt_record(data: bytes) -> bytes:
    cipher = AES.new(KEY, AES.MODE_ECB)
    padding = 16 - (len(data) % 16)
    data = data + bytes([padding]) * padding
    return cipher.encrypt(data)

def decrypt_record(data: bytes) -> bytes:
    cipher = AES.new(KEY, AES.MODE_ECB)
    plaintext = cipher.decrypt(data)
    padding = plaintext[-1]
    return plaintext[:-padding]

# Ground Truth

| File | Rule | Misuse |
|---|---|---|
| app/auth.py | CR1 | MD5/SHA1 in password context |
| app/encryption.py | CR2 | AES ECB |
| app/crypto_utils.py | CR3 | Constant IV |
| app/passwords.py | CR4 | Static salt + 1000 PBKDF2 iterations + direct SHA256 |
| app/tokens.py | CR5 | random module for security tokens |

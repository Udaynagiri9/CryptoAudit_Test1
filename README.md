# CryptoAudit Demo Repository

Deliberately vulnerable Python repository for CryptoAudit demonstration.

Cases:
- CR1: weak password hashing
- CR2: AES ECB mode
- CR3: static IV/nonce
- CR4: weak PBKDF2 + static salt
- CR5: insecure randomness for security tokens

DO NOT use this repository in production.
See GROUND_TRUTH.md for expected findings.

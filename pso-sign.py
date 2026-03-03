from hashlib import sha256
data = b"My super secret contract text 2026"
digest = sha256(data).digest()

print(digest.hex())  # <-- this 32-byte value is what you actually send to PSO

data = b"My super secret contract text 2026 nr2"
digest = sha256(data).digest()

print(digest.hex())  # <-- this 32-byte value is what you actually send to PSO
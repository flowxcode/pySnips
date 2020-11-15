# hash games

import hashlib
import os

str = "testpw"
stre = str.encode('utf-8')
print(str)
print(stre)

#w = hashlib.sha1(str)
x = hashlib.sha1(stre)

print(x.digest())
print(x.hexdigest())

### snip2
salt = os.urandom(32) # Remember this
password = 'password123'

key = hashlib.pbkdf2_hmac(
    'sha256', # The hash digest algorithm for HMAC
    password.encode('utf-8'), # Convert the password to bytes
    salt, # Provide the salt
    100000 # It is recommended to use at least 100,000 iterations of SHA-256 
)

# print(key)

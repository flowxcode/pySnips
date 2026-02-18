import zlib
import struct

data = b'UserCertData:ID=98765,Expiry=2030'

# How the card would store it (correct way)
stored_crc = zlib.crc32(data) & 0xFFFFFFFF
print(f"Stored CRC value: {hex(stored_crc)}")

def verify_correct(data, stored_crc):
    computed = zlib.crc32(data) & 0xFFFFFFFF
    return computed == stored_crc   # direct match → true when intact

def verify_wrong(data, stored_crc):
    # The transmission-style check that fails here
    appended = data + struct.pack('<I', stored_crc)  # little-endian, common mistake
    computed_whole = zlib.crc32(appended) & 0xFFFFFFFF
    return computed_whole == 0   # almost never true!

print("Correct verification (should pass):", verify_correct(data, stored_crc))
print("Wrong verification (will fail even on perfect data):", verify_wrong(data, stored_crc))

# Now corrupt one byte
corrupted = data[:-1] + b'X'
print("Correct verification on corrupted data:", verify_correct(corrupted, stored_crc))

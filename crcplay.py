import zlib

def compute_crc(data_bytes):
    return zlib.crc32(data_bytes) & 0xFFFFFFFF  # standard CRC-32, unsigned

# Example payload you might store inside a credential
data = b'Identity data: UserID=12345, CertSerial=ABCDEF'

stored_crc = compute_crc(data)
print(f"Computed and stored CRC: {hex(stored_crc)}")

def verify_integrity(data, stored_crc):
    if compute_crc(data) == stored_crc:
        print("Integrity check passed – data is intact.")
        return True
    else:
        print("Integrity check FAILED – initiating card/security reset!")
        # In real card code: call reset routine here
        return False

# Normal case
verify_integrity(data, stored_crc)

# Simulate corruption (e.g., one bit flipped by fault)
corrupted_data = data[:-1] + b'X'
verify_integrity(corrupted_data, stored_crc)

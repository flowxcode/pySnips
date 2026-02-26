import struct

def sm_wrap(cmd: bytes, enc_key: bytes, mac_key: bytes, ssc: bytes) -> bytes:
    """Realistic ISO 7816 SM wrapper (toy crypto) - SSC now used in MAC demo"""
    # Force SM bit in CLA (0C for interindustry class)
    cla = (cmd[0] & 0x0F) | 0x0C
    header = bytes([cla]) + cmd[1:4]          # 0C 20 00 81
    data = cmd[5:] if len(cmd) > 5 else b''

    # 1. ISO padding + encrypt (placeholder)
    pad_len = (16 - (len(data) + 1) % 16) % 16
    padded = data + b'\x80' + b'\x00' * pad_len
    enc = b'ENCRYPTED_' + padded[:8]          # still fake, but correct length

    # 2. Build cryptogram TLV
    cryptogram = b'\x87' + struct.pack('B', len(enc) + 1) + b'\x01' + enc

    # 3. MAC input = SSC || header || cryptogram   ← this is the key line!
    mac_input = ssc + header + cryptogram
    # Real MAC would be: CMAC(mac_key, mac_input)[:8] or Retail-MAC
    mac = (b'MAC' + ssc[:5])[:8]              # fake but now contains SSC so unique!

    # 4. MAC TLV
    mac_tlv = b'\x8E\x08' + mac

    # 5. Final SM payload
    sm_data = cryptogram + mac_tlv
    return header + bytes([len(sm_data)]) + sm_data


# Try it with real SSC from GET CHALLENGE
ssc = b'\x12\x34\x56\x78\x9A\xBC\xDE\xF0'   # 8 bytes typical for 3DES/AES
wrapped = sm_wrap(b'\x00\x20\x00\x81\x08\x31\x32\x33\x34\x35\x36\x37\x38',
                  b'', b'', ssc)

print("Wrapped APDU (hex):", wrapped.hex())
print("SSC used in MAC:", (b'MAC' + ssc[:5]).hex())  # you can see it changed!

import sys

# Read bytes from stdin
data = sys.stdin.buffer.read()

# Dict to count bytes frequency {byte_chr: freq}
freqs = {}

def is_ascii_printable(character: str) -> bool:
    return character.isascii() and character.isprintable()

def byte_repr(b: int) -> str:
    character = chr(b)
    if is_ascii_printable(character):
        return character
    return f"\\x{b:02x}"

def count_bytes_freq(datos_bytes: bytes):
    for b in datos_bytes:
        freqs[b] = freqs.get(b, 0) + 1

count_bytes_freq(data)

# Order by numeric val from key rows
freqs_ordered = sorted(freqs.items(), key=lambda item: item[0])

for byte_val, frecuencia in freqs_ordered:
    representacion = byte_repr(byte_val)
    print(f"{representacion} {frecuencia}")
import sys
import re

# Run-length encoding (byte-pair form).
# Input commands per line:
#   ENCODE <text>   -> print encoded form like "5A 3B 2C 1D"
#   DECODE <enc>    -> decode back to original
# byte_repr: literal char (32..126) or \xHH for others.

def is_ascii_printable(character: str) -> bool:
    return character.isascii() and character.isprintable()

def byte_repr(b):
    character = chr(b)
    if is_ascii_printable(character):
        return character
    return f"\\x{b:02x}"

def rle_encode(data):
    freqs = {}
    result = []

    for byte in data:
        freqs[byte] = freqs.get(byte, 0) + 1
    for byte_val, freq in freqs.items():
        #repr = byte_repr(byte_val)
        result.append(f"{freq}{byte_val}")

    return result

def rle_decode(tokens):
    result = ""
    for token in tokens:
        match = re.match(r"^([0-9])([A-Za-z])$", token)
        if match:
            number = int(match.group(1))
            letter = match.group(2)

            for _ in range(number):
                result += letter

    return result

for raw in sys.stdin:
    line = raw.rstrip("\n")
    if not line:
        continue

    splitted_line = line.split(" ")

    match splitted_line[0]:
        case "ENCODE": 
            result = rle_encode(splitted_line[1])
            print(f"{" ".join(result)}")
        case "DECODE":
            result = rle_decode(splitted_line[1:])
            print(f"{result}")
        case _:
            break
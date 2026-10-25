import sys
import re

def is_ascii_printable(character: str) -> bool:
    return character.isascii() and character.isprintable()

def byte_repr(b: str) -> str:
    if is_ascii_printable(b):
        return b
    return f"\\x{ord(b):02x}"

def rle_encode(data):
    if not data:
        return []
    
    result = []
    current_char = data[0]
    count = 1
    
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            rep = byte_repr(current_char)
            result.append(f"{count}{rep}")
            current_char = char
            count = 1
            

    rep = byte_repr(current_char)
    result.append(f"{count}{rep}")
    
    return result

def rle_decode(tokens):
    result = ""
    for token in tokens:
        match = re.match(r"^([0-9]+)(.+)$", token)
        if match:
            number = int(match.group(1))
            char = match.group(2)
            result += char * number
    return result

for raw in sys.stdin:
    line = raw.rstrip("\n")
    if not line:
        continue

    splitted_line = line.split(" ")

    match splitted_line[0]:
        case "ENCODE": 
            text = " ".join(splitted_line[1:])
            result = rle_encode(text)
            print(" ".join(result))
        case "DECODE":
            result = rle_decode(splitted_line[1:])
            print(result)
        case _:
            break
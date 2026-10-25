import sys

def is_ascii_printable(character: str) -> bool:
    return character.isascii() and character.isprintable()

def byte_repr(b: int) -> str:
    character = chr(b)
    if is_ascii_printable(character):
        return character
    return f"\\x{b:02x}"

def huffman_decode(lines: list[str], n, bit_string: str) -> str:
    result = ""
    for line in range(n):
        line_splitted = lines[line].split(' ')
        line_byte: int = int(line_splitted[0])
        line_code: str = line_splitted[1]

        character = byte_repr(line_byte)
        result += character
        if bit_string.startswith(line_code):
            bit_string = bit_string[len(line_code):]

    if bit_string != "":
        result = "ERR tuncated"

    return result
lines = sys.stdin.read().splitlines()
if not lines:
    sys.exit(0)

n = int(lines[0].strip())
bit_string = lines[-1]

result = huffman_decode(lines[1:], n, bit_string)
print(result)
import sys

def is_ascii_printable(character: str) -> bool:
    return character.isascii() and character.isprintable()

def byte_repr(b: int) -> str:
    character = chr(b)
    if is_ascii_printable(character):
        return character
    return f"\\x{b:02x}"

def huffman_decode(lines: list[str], n, bit_string: str) -> str:
    code_to_char = {}
    for i in range(n):
        line_splitted = lines[i].split(' ')
        line_byte: int = int(line_splitted[0])
        line_code: str = line_splitted[1]
        code_to_char[line_code] = byte_repr(line_byte)

    result = ""
    current_code = ""

    for bit in bit_string:
        current_code += bit

        if current_code in code_to_char:
            result += code_to_char[current_code]
            current_code = ""
        
    if current_code != "":
        return "ERR tuncated"
    
    return result

lines = sys.stdin.read().splitlines()
if not lines:
    sys.exit(0)

n = int(lines[0].strip())
bit_string = lines[-1]

result = huffman_decode(lines[1:n+1], n, bit_string)
print(result)
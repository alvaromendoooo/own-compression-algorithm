import sys

# Read raw bytes from stdin and print one line per unique byte:
#   <byte_repr> <count>
# sorted by byte value ascending.
# byte_repr: literal char if 32..126, else \xHH
#
# Example:  hello -> e 1 / h 1 / l 2 / o 1

data = sys.stdin.buffer.read()

# TODO: count byte frequencies
freqs = {}

def byte_repr(b):
    # TODO: return printable char or \xHH
    return ""

# TODO: print sorted output

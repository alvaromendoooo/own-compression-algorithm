import sys

# Canonical Huffman (RFC 1951 sec 3.2.2):
# given only the BIT LENGTH of each symbol's code, reconstruct the codes
# deterministically. This is what DEFLATE actually stores in the header.
#
# Input: lines of "<symbol> <code_length>".
# Output: lines of "<symbol> <canonical_code>" sorted by symbol asc.
#
# Algorithm (3 steps):
#   1. Count how many codes have each length: bl_count[L].
#   2. Compute starting code for each length:
#        code = 0
#        for L in 1..MAX:
#          code = (code + bl_count[L-1]) << 1
#          next_code[L] = code
#   3. Assign codes to symbols sorted by (length, symbol).

def cannonical_huffman(lengths: dict):
    # Filter unused symbols
    active_lengths = {sym: l for sym, l in lengths.items() if l > 0}
    if not active_lengths:
        return

    max_length = max(active_lengths.values())

    # 1. Count how many codes have each length
    bl_count = {}
    for l in active_lengths.values():
        bl_count[l] = bl_count.get(l, 0) + 1

    # 2. Compute starting code for each length
    next_code = {}
    code = 0
    for bits in range(1, max_length + 1):
        code = (code + bl_count.get(bits - 1, 0)) << 1
        next_code[bits] = code

    # 3. Assing codes to symbols sorted by (length, symbol)
    sorted_symbs = sorted(active_lengths.keys(), key = lambda s: (active_lengths[s], s))
    cannonical_codes = {}
    for sym in sorted_symbs:
        length = active_lengths[sym]
        cannonical_codes[sym] = format(next_code[length], f"0{length}b")
        next_code[length] += 1

    for sym in sorted(cannonical_codes.keys()):
        print(f"{sym} {cannonical_codes[sym]}")

lines = sys.stdin.read().splitlines()
lengths = {}

for line in lines:
    line_split = line.split(" ")
    sym = line_split[0]
    len = int(line_split[1])

    lengths[sym] = len

cannonical_huffman(lengths)

import sys
import math
from collections import Counter

# Read bytes from stdin, output:
#   bytes=<n>
#   entropy=<H>      (4 decimal places, bits per byte)
#   min_size=<bytes> (3 decimal places, theoretical min compressed size in bytes)
# H(X) = -sum(p * log2(p)) over each unique byte.

data = sys.stdin.buffer.read()
total_bytes = len(data)

# Non-bytes entry case
if total_bytes == 0:
    print(f"bytes={total_bytes}")
    print(f"entropy=0.0000")
    print(f"min_size=0.000")
    sys.exit(0)

# Get the frequency of unique iput bytes
freqs = Counter(data)

# Shannon entropy calc.
# H -= p * log2(p)
H = 0.0
for count in freqs.values():
    p = count / total_bytes
    H -= p * math.log2(p)

# Calc the theorical compressed size
min_size = (H * total_bytes) / 8

print(f"bytes={total_bytes}")
print(f"entropy={H:.4f}")
print(f"min_size={min_size:.3}")
import sys
import heapq
from collections import Counter

# Build a Huffman code from byte frequencies; print sorted by byte value:
#   <byte_repr> <code>
# Tie-breaking: smaller byte first, leaves before internal nodes.
# Single-byte input: code is "0".

def is_ascii_printable(character: str) -> bool:
    return character.isascii() and character.isprintable()

def byte_repr(b: int) -> str:
    character = chr(b)
    if is_ascii_printable(character):
        return character
    return f"\\x{b:02x}"

class Node:
    def __init__(self, freq, byte = None, left = None, right = None, order = 0):
        self.freq = freq
        self.byte = byte
        self.left = left
        self.right = right
        self.order = order

    # Definition of how nodes are compared in heap
    # CRITERIA: Least freq first. In case ==, least order/byte.
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq

        self_is_leaf = self.byte is not None
        other_is_leaf = other.byte is not None

        if self_is_leaf != other_is_leaf:
            return self_is_leaf

        if self_is_leaf and other_is_leaf:
            return self.byte < other.byte

        return self.order < other.order

def huffman_algorithm(freqs: dict):
    if not freqs:
        return {}

    # Defining an empty queue
    min_heap = []
    counter = 0

    # 1-2. Each detected symbol as a leaf
    for byte_val, freq in freqs.items():
        node = Node(freq = freq, byte = byte_val, order = counter)
        # Push each leaf in defined queue
        # The register takes into account min-order
        heapq.heappush(min_heap, node)
        counter += 1

    if len(freqs) == 1:
        only_byte = list(freqs.keys())[0]
        return {only_byte: "0"}

    # 3. Repeat until one node left (root val)
    while len(min_heap) > 1:
        # 3.1 Pop the two smallest-frequency nodes
        left_node = heapq.heappop(min_heap)
        right_node = heapq.heappop(min_heap)

        # 3.2 Create parent node
        parent_node = Node(
            freq = left_node.freq + right_node.freq,
            left = left_node,
            right = right_node,
            order = counter
        )
        counter += 1

        # 3.3 Insert parent node into heap
        heapq.heappush(min_heap, parent_node)


    # 4. Generating codes iterating recursively the tree
    codes = {}

    def generate_codes(node: Node, current_code = ""):
        if node is None:
            return

        # If node is a leave, we save it's code
        if node.byte is not None:
            codes[node.byte] = current_code
            return

        # Iterating through left and right child in parents node
        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")

    root = min_heap[0]
    generate_codes(root, "") # Iterate from the top of the tree till leaves are found
    return codes

data = sys.stdin.buffer.read()
freqs = dict(Counter(data))

codes = huffman_algorithm(freqs)

for b in sorted(codes.keys()):
    print(f"{byte_repr(b)} {codes[b]}")

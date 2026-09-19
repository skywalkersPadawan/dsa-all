"""
Huffman Coding (Greedy Compression Algorithm)

What it is:
A lossless data compression algorithm. It assigns variable-length prefix codes to characters
based on their frequencies: frequently occurring characters receive shorter codes, and
rare characters receive longer codes.

When it is used:
- Lossless file compression (ZIP, GZIP, JPEG, MP3 entropy encoding).
- Demonstrates greedy priority-queue tree construction.

The Key Idea:
Greedy Merge via Min-Heap:
1. Count character frequencies.
2. Build a min-heap where each node is a leaf `(frequency, char)`.
3. While the heap has more than one node:
   - Extract the two nodes with the lowest frequencies: `left` and `right`.
   - Create a new internal node with `frequency = left.freq + right.freq`.
   - Push this internal node back into the min-heap.
4. The remaining single node is the root of the Huffman Tree.
5. Traverse the tree: assign '0' to left branch and '1' to right branch to build codes.

Prefix Property:
No character's code is a prefix of any other character's code, guaranteeing unique decodability!

Time Complexity:
- O(k log k) where k is the number of unique characters.

Space Complexity:
- O(k) for the Huffman tree.
"""

from collections import Counter
import heapq
from typing import Optional


class HuffmanNode:
    def __init__(
        self,
        freq: int,
        char: Optional[str] = None,
        left: Optional["HuffmanNode"] = None,
        right: Optional["HuffmanNode"] = None,
    ):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other: "HuffmanNode") -> bool:
        # Comparison method for heapq ordering
        return self.freq < other.freq


def build_huffman_codes(text: str) -> dict[str, str]:
    """Generates optimal prefix codes for characters in text."""
    if not text:
        return {}

    frequency = Counter(text)

    # Edge case: only one distinct character
    if len(frequency) == 1:
        char = next(iter(frequency))
        return {char: "0"}

    # Initialize min-heap with leaf nodes
    min_heap: list[HuffmanNode] = [
        HuffmanNode(freq=f, char=c) for c, f in frequency.items()
    ]
    heapq.heapify(min_heap)

    # Combine two lowest frequency nodes iteratively
    while len(min_heap) > 1:
        left = heapq.heappop(min_heap)
        right = heapq.heappop(min_heap)

        parent = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(min_heap, parent)

    root = min_heap[0]
    codes: dict[str, str] = {}

    def generate_codes(node: Optional[HuffmanNode], current_code: str) -> None:
        if not node:
            return
        if node.char is not None:
            codes[node.char] = current_code
            return

        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")

    generate_codes(root, "")
    return codes


if __name__ == "__main__":
    text = "abracadabra"
    codes = build_huffman_codes(text)

    # 'a' appears 5 times (most frequent), should have the shortest or tied-shortest code
    assert len(codes["a"]) <= len(codes["b"])
    assert len(codes["a"]) <= len(codes["c"])

    # Verify prefix property: no code is a prefix of another
    code_list = list(codes.values())
    for i, c1 in enumerate(code_list):
        for j, c2 in enumerate(code_list):
            if i != j:
                assert not c1.startswith(
                    c2
                ), f"{c2} is a prefix of {c1} (violates prefix property)"

    print("All Huffman Coding tests passed successfully.")

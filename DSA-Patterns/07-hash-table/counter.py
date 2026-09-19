"""
Python `collections.Counter` Pattern

What it is:
A specialized `dict` subclass from Python's standard library designed specifically
for counting hashable objects. Elements are stored as dictionary keys and their counts
are stored as dictionary values.

When it is used:
- Rapid frequency counting in coding interviews without manual `counts[x] = counts.get(x, 0) + 1`.
- Finding top-k most frequent elements via `.most_common(k)`.
- Anagram / multiset equality checks (`Counter(s) == Counter(t)`).
- Counting differences / multisets arithmetic.

The Key Idea:
- Accessing a missing key returns `0` instead of raising `KeyError`.
- Useful methods:
  - `counter.most_common(k)`: returns list of top k `(element, count)` tuples in O(n log k).
  - `counter.elements()`: iterator over elements repeating each as many times as its count.
  - Arithmetic: `c1 + c2`, `c1 - c2`, `c1 & c2` (min of counts), `c1 | c2` (max of counts).

Time Complexity:
- Construction from iterable: O(n).
- Access / Lookup: O(1) average.
- `most_common(k)`: O(n log k) using a heap internally.

Space Complexity:
- O(distinct_elements) auxiliary space.
"""

from collections import Counter


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Returns the k most frequent elements in nums.

    (LeetCode 347)
    Time: O(n log k), Space: O(n).
    """
    counts = Counter(nums)

    # most_common(k) returns [(elem, count), ...]
    return [element for element, _ in counts.most_common(k)]


def can_construct_ransom_note(ransom_note: str, magazine: str) -> bool:
    """Returns True if ransom_note can be constructed using characters from magazine.

    (LeetCode 383)
    """
    ransom_counts = Counter(ransom_note)
    magazine_counts = Counter(magazine)

    # Counter subtraction: (ransom_counts - magazine_counts) is empty if magazine has all required counts
    return len(ransom_counts - magazine_counts) == 0


if __name__ == "__main__":
    # Top-K frequent
    nums = [1, 1, 1, 2, 2, 3]
    assert top_k_frequent(nums, 2) == [1, 2]

    # Ransom note test
    assert can_construct_ransom_note("a", "b") is False
    assert can_construct_ransom_note("aa", "ab") is False
    assert can_construct_ransom_note("aa", "aab") is True

    # Counter arithmetic
    c1 = Counter(a=3, b=1)
    c2 = Counter(a=1, b=2)
    assert c1 + c2 == Counter(a=4, b=3)
    assert c1 - c2 == Counter(a=2)  # counts <= 0 are excluded

    print("All Counter tests passed successfully.")

"""
Frequency Map Pattern

What it is:
A pattern where a hash map is used to count the occurrences (frequencies)
of elements in a sequence.

When it is used:
- Finding the most frequent element (majority element).
- Anagram detection (two strings are anagrams if their frequency maps match).
- First unique character in a string.
- Finding duplicates.

The Key Idea:
Iterate through the collection.
Update frequency map: `counts[item] = counts.get(item, 0) + 1`.

Time Complexity:
- O(n) to build the frequency map across an array of length n.
- O(1) average lookup for any element's frequency.

Space Complexity:
- O(k) where k is the number of distinct elements (k <= n).
"""


def build_frequency_map(items: list[int | str]) -> dict[int | str, int]:
    """Constructs a frequency dictionary using standard dict and .get()."""
    counts: dict[int | str, int] = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


def is_anagram(s: str, t: str) -> bool:
    """Checks if t is an anagram of s using a frequency map.

    (LeetCode 242)
    Time: O(n), Space: O(1) since English alphabet is 26 chars.
    """
    if len(s) != len(t):
        return False

    counts: dict[str, int] = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    for char in t:
        if char not in counts or counts[char] == 0:
            return False
        counts[char] -= 1

    return True


def first_unique_char(s: str) -> int:
    """Returns the index of the first non-repeating character, or -1.

    (LeetCode 387)
    Time: O(n), Space: O(1).
    """
    counts: dict[str, int] = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    for index, char in enumerate(s):
        if counts[char] == 1:
            return index

    return -1


if __name__ == "__main__":
    freq = build_frequency_map(
        ["apple", "banana", "apple", "orange", "banana", "apple"]
    )
    assert freq["apple"] == 3
    assert freq["banana"] == 2
    assert freq["orange"] == 1

    # Anagram tests
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False

    # First unique char
    assert first_unique_char("leetcode") == 0  # 'l'
    assert first_unique_char("loveleetcode") == 2  # 'v'
    assert first_unique_char("aabb") == -1

    print("All Frequency Map tests passed successfully.")

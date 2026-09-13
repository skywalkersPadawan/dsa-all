"""
Trie (Prefix Tree) Data Structure

What it is:
A tree-like data structure used for efficient retrieval and storage of strings over an alphabet.
Every node represents a common prefix shared by one or more keys.

When it is used:
- Autocomplete, typeahead, and predictive text search.
- IP routing (longest prefix matching).
- Spell checkers.
- Word Search II (LeetCode 212 - Trie + Backtracking).
- Design Add and Search Words Data Structure (LeetCode 211).
- Implement Trie (LeetCode 208).

The Key Idea:
TrieNode:
- `children`: dictionary or array of size 26 mapping `char -> TrieNode`.
- `is_end_of_word`: boolean flag marking whether a word terminates at this node.

Operations:
1. `insert(word)`: walk down character by character, creating nodes if they don't exist.
   Mark last node with `is_end_of_word = True`.
2. `search(word)`: walk down matching characters. Returns True if last node exists AND `is_end_of_word == True`.
3. `starts_with(prefix)`: walk down matching characters. Returns True if all characters of prefix exist in the Trie.

Time Complexity:
- Insert: O(L) where L is length of word.
- Search: O(L).
- StartsWith: O(L).

Space Complexity:
- O(N * L * alphabet_size) in worst case (no common prefixes), but much smaller in practice due to shared prefixes.
"""


class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.is_end_of_word: bool = False


class Trie:
    """Standard Trie (Prefix Tree) implementation."""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts a word into the trie. O(L)."""
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        """Returns True if the word is in the trie, False otherwise. O(L)."""
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """Returns True if there is any word in the trie that starts with prefix. O(L)."""
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False  # "app" is only a prefix, not a full word
    assert trie.starts_with("app") is True

    trie.insert("app")
    assert trie.search("app") is True

    assert trie.search("banana") is False
    assert trie.starts_with("ban") is False

    print("All Trie tests passed successfully.")

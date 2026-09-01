from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        # Build Trie
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows, cols = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return

            nxt = node.children[ch]
            if nxt.word:
                res.append(nxt.word)
                nxt.word = None

            board[r][c] = "#"
            if r > 0 and board[r - 1][c] != "#":
                dfs(r - 1, c, nxt)
            if r < rows - 1 and board[r + 1][c] != "#":
                dfs(r + 1, c, nxt)
            if c > 0 and board[r][c - 1] != "#":
                dfs(r, c - 1, nxt)
            if c < cols - 1 and board[r][c + 1] != "#":
                dfs(r, c + 1, nxt)

            board[r][c] = ch
            if not nxt.children and nxt.word is None:
                del node.children[ch]

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)

        return res


# study this solution naive approach will be too slow and memory intensive

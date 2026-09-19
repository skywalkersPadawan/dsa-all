"""
Valid Parentheses Pattern

What it is:
Determines whether a string containing brackets '(', ')', '{', '}', '[', ']' is valid:
1. Open brackets must be closed by the same type of closing brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

When it is used:
- LeetCode 20 (Valid Parentheses).
- Compiler syntax checking / code linting.
- Mathematical expression evaluation.

The Key Idea:
Use a LIFO Stack and a closing-to-opening bracket hash map:
- If character is an open bracket: push onto stack.
- If character is a closing bracket:
  - If stack is empty -> invalid (closing bracket has no matching opening bracket).
  - Pop top of stack. If it does not match the expected open bracket -> invalid.
- At the end: stack must be empty (all opened brackets were closed).

Time Complexity:
- O(n) single pass over the string.

Space Complexity:
- O(n) auxiliary space for the stack in the worst case (e.g. all open brackets).

Common Pitfalls / Edge Cases:
- String starts with a closing bracket (e.g., `"]"`): stack is empty when popping.
- String ends with unmatched opening brackets (e.g., `"("`): stack is not empty at end.
- Odd length strings can immediately return False.
"""


def is_valid_parentheses(s: str) -> bool:
    """Checks if parentheses string s is valid in O(n) time and O(n) space."""
    if len(s) % 2 != 0:
        return False

    matching_bracket = {")": "(", "}": "{", "]": "["}
    stack: list[str] = []
    for char in s:
        if char in matching_bracket:
            # char is a closing bracket
            if not stack or stack[-1] != matching_bracket[char]:
                return False
            stack.pop()
        else:
            # char is an opening bracket
            stack.append(char)

    return len(stack) == 0


if __name__ == "__main__":
    # Valid cases
    assert is_valid_parentheses("()") is True
    assert is_valid_parentheses("()[]{}") is True
    assert is_valid_parentheses("{[()]}") is True
    assert is_valid_parentheses("") is True

    # Invalid cases
    assert is_valid_parentheses("(]") is False
    assert is_valid_parentheses("([)]") is False
    assert is_valid_parentheses("]") is False
    assert is_valid_parentheses("(") is False
    assert is_valid_parentheses("(((") is False

    print("All Valid Parentheses tests passed successfully.")

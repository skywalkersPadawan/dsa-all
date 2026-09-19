# Self-Balancing Binary Search Trees

## Overview

A standard Binary Search Tree (BST) provides `O(h)` search, insertion, and deletion. However, if keys are inserted in sorted order, the tree degenerates into a linear linked list with height h = n, degrading all operations to `O(n)`.

Self-balancing BSTs maintain a height of `O(log n)` through tree **rotations** whenever insertions or deletions violate specific balance invariants.

---

## 1. AVL Trees (Adelson-Velsky and Landis)

### Balance Invariant:

For every node, the height difference between its left and right subtrees (the **Balance Factor**) must be at most 1:

`Balance Factor(node) = height(node.left) - height(node.right) in {-1, 0, 1}`

### The 4 Rotation Cases:

When a violation occurs (Balance Factor is -2 or 2):

1. **Left-Left (LL) Case:** Inserted into left subtree of left child.
   - **Fix:** Single **Right Rotation** at grandparent.
2. **Right-Right (RR) Case:** Inserted into right subtree of right child.
   - **Fix:** Single **Left Rotation** at grandparent.
3. **Left-Right (LR) Case:** Inserted into right subtree of left child.
   - **Fix:** **Left Rotation** on child, followed by **Right Rotation** on grandparent.
4. **Right-Left (RL) Case:** Inserted into left subtree of right child.
   - **Fix:** **Right Rotation** on child, followed by **Left Rotation** on grandparent.

### Characteristics:

- Strictly balanced (height <= 1.44 \* log2(n)).
- Faster lookups than Red-Black trees due to tighter height bounds.
- Slower insertions and deletions due to more frequent rotations.

---

## 2. Red-Black Trees

### Invariants:

1. Every node is either **Red** or **Black**.
2. The root is always **Black**.
3. All leaf nodes (`NIL` sentinels) are **Black**.
4. If a node is **Red**, both of its children must be **Black** (No two consecutive red nodes on any path).
5. For each node, every simple path from the node to any descendant `NIL` leaf contains the exact same number of black nodes (**Black-Height**).

### Characteristics:

- Relaxed balance (the longest path is at most twice as long as the shortest path).
- Maximum height <= 2 \* log2(n + 1).
- Requires at most 2 rotations for an insertion and at most 3 rotations for a deletion.
- Preferred for general-purpose maps and sets across major standard libraries:
  - C++ `std::map` / `std::set`
  - Java `TreeMap` / `TreeSet`
  - Linux kernel CFS scheduler

---

## Summary Comparison

| Feature                | AVL Tree                | Red-Black Tree                |
| :--------------------- | :---------------------- | :---------------------------- |
| **Strictness**         | Strictly balanced       | Approximately balanced        |
| **Height Bound**       | ~ 1.44 log n            | ~ 2 log n                     |
| **Lookup Performance** | Faster (shorter tree)   | Slightly slower               |
| **Insert / Delete**    | Slower (more rotations) | Faster (fewer rotations)      |
| **Best Used When**     | Lookups dominate writes | Frequent insertions/deletions |

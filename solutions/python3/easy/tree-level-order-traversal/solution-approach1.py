# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/bca3g-20-07-26-hackathon3/challenges/tree-level-order-traversal/problem?isFullScreen=true
# Problem     Tree: Level Order Traversal
# Difficulty  Easy
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-20, 11:33 a.m.
# ──────────────────────────────────────────────────



"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
    #Write your code heredef levelOrder(root):
    if root is None:
        return

    queue = [root]
    result = []

    while queue:
        current = queue.pop(0)

        result.append(current.info)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    print(*result)
def levelOrder(root):
    if root is None:
        return

    queue = [root]
    result = []

    while queue:
        current = queue.pop(0)

        result.append(current.info)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    print(*result)

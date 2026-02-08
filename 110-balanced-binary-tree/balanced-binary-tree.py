# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def high(node):
            if not node:
                return 0
            else:
                return 1 + max(high(node.left), high(node.right))
        if abs(high(root.left) - high(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False

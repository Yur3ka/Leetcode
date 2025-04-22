# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        level = []
        temp = root
        if not root:
            return True
        level.append(temp)
        while level:
            stack = []
            next_level = []
            for node in level:
                if not node.left:
                    stack.append(-101)
                else:
                    stack.append(node.left.val)
                    next_level.append(node.left)
                if not node.right:
                    stack.append(-101)
                else:
                    stack.append(node.right.val)
                    next_level.append(node.right)
            n = len(stack)
            for i in range(n):
                if stack[i] != stack[n-i-1]:
                    return False
            level = next_level
            next_level = []
        return True
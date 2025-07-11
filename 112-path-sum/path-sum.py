# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        value = set()
        if not root:
            return False
        def dfs(root,curr):
            if not root:
                return
            if not root.left and not root.right:
                value.add(curr+root.val)
            left = dfs(root.left,curr + root.val)
            right = dfs(root.right,curr + root.val)
        dfs(root,0)
        print(value)
        return targetSum in value
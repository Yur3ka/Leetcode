# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        ans = -float('inf')
        value = set()
        MOD = 10**9+7
        def sumTree(node):
            if not node:
                return 0
            left = sumTree(node.left)
            right = sumTree(node.right)
            curr_node = left + right + node.val
            value.add(curr_node)
            return curr_node
        total = sumTree(root)
        for val in value:
            temp = (total -val)*val
            ans = max(ans,temp)
        return ans%MOD
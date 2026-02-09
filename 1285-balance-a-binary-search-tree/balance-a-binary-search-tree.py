# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nums = []
        if not root: 
            return root

        def inOrder(node):
            if not node:
                return
            if node.left:
                inOrder(node.left)
            nums.append(node.val)
            if node.right:
                inOrder(node.right)
        inOrder(root)
        
        def balance(arr):
            if not arr:
                return
            k = len(arr)//2 
            node = TreeNode(arr[k])
            node.left = balance(arr[:k])
            node.right = balance(arr[k+1:])
            return node
        node = balance(nums)
        return node
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if not root:
            return ans
        queue = [root]
        while queue:
            current = queue.pop()
            ans += 1
            if current.left == None and current.right == None:
                continue
            elif current.right == None:
                queue.append(current.left)
            else:
                queue.append(current.left)
                queue.append(current.right)
        return ans
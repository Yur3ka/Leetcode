# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = -float('inf')
        ans_lv = 1
        stack = [root]
        level_sum = 0
        level = 1
        temp = []
        while stack:
            curr = stack.pop()
            level_sum += curr.val
            if curr.left:
                temp.append(curr.left)
            if curr.right:
                temp.append(curr.right)
            if len(stack) == 0:
                stack = temp[:]
                # print(level_sum)
                temp = []
                if level_sum > ans:
                    ans_lv = level
                    ans = level_sum
                level_sum = 0
                level += 1
                
        return ans_lv

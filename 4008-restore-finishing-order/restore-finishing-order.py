class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        fr = set(friends)
        ans = []
        for o in order:
            if o in fr:
                ans.append(o)
        return ans
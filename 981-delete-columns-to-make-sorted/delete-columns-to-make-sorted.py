class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        # strs.sort()
        for i in range(len(strs[0])):
            status = True
            for j in range(len(strs)-1):
                if strs[j][i]> strs[j+1][i]:
                    status = False
                    break
            if not status:
                ans += 1
        return ans
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        pres = []
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            pres.append(curr)
        ans = []
        for q in queries:
            c= bisect_right(pres,q)
            ans.append(c)
        return ans
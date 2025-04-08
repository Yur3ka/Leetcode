class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        existed = set()
        cut = -1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] in existed:
                cut = i
                break
            else:
                existed.add(nums[i])
        if cut == -1:
            return 0
        ans = cut //3 + 1
        return ans
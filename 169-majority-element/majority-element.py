class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = Counter(nums)
        for k,v in count.items():
            if v > n/2:
                return k
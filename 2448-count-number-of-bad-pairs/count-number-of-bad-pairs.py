class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        vector = collections.defaultdict(int)
        for i in range(len(nums)):
            vector[nums[i] - i] += 1
        total_pairs = len(nums)*(len(nums)-1)//2
        for _, val in vector.items():
            if val >=2:
                total_pairs -= val*(val-1)//2
        return total_pairs
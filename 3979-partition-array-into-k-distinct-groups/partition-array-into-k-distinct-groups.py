class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        c = Counter(nums)
        n = len(nums)
        if n % k != 0:
            return False
        for _,v in c.items():
            if v > n//k:
                return False
        return True
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        used = set(nums)
        curr = k
        while True:
            if curr not in used:
                return curr
            curr += k
        
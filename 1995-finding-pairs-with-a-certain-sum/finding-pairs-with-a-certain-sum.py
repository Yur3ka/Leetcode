class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        
        self.n2 = nums2
        self.c1 = Counter(nums1)
        self.c2 = Counter(nums2)
    def add(self, index: int, val: int) -> None:
        before = self.n2[index]
        after = before+val
        self.c2[before] -= 1
        self.c2[after] = self.c2.get(after,0)+1
        self.n2[index] = after

    def count(self, tot: int) -> int:
        ans = 0
        for k, v in self.c1.items():
            if tot-k in self.c2:
                ans += v*self.c2[tot-k]
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
class NumArray:
    pre = []
    def __init__(self, nums: List[int]):
        curr = 0
        self.pre = []
        for n in nums:
            curr += n
            self.pre.append(curr)

    def sumRange(self, left: int, right: int) -> int:
        if left -1 >= 0:
            l = self.pre[left-1]
        else:
            l = 0
        r = self.pre[right]
        print(r,l)
        return r-l


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
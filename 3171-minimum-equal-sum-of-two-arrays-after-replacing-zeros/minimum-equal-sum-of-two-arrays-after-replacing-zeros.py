class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        zero1 = nums1.count(0)
        zero2 = nums2.count(0)
        if zero1 == 0 and zero2 == 0:
            if sum1 == sum2:
                return sum1
        elif zero1 == 0:
            if sum1 >= sum2 + zero2:
                return sum1
        elif zero2 == 0:
            if sum2 >= sum1 + zero1: 
                return sum2
        else:
            return max(sum1+zero1,sum2+zero2)
        return -1
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = [[],[]]
        n1 = set(nums1)
        n2 = set(nums2)
        for n in n1:
            if n not in n2:
                res[0].append(n)
        for n in n2:
            if n not in n1:
                res[1].append(n)
        return res
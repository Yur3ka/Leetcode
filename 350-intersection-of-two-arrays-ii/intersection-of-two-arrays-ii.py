class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        for k,v in c1.items():
            if k in c2:
                ans += [k]*(min(v,c2[k]))
        return ans
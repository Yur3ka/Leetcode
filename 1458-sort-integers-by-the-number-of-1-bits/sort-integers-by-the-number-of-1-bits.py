class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        c = defaultdict(list)
        for i in arr:
            k = str(bin(i)).count('1')
            c[k].append(i)
        v = sorted(c.keys())
        ans = []
        for key in v:
            ans.extend(c[key])
        return ans
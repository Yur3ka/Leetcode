class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s).items()
        a = list(counter)
        odd = []
        even = []
        for key, val in a:
            if val % 2 == 0:
                even.append(val)
            else:
                odd.append(val)
        odd.sort()
        even.sort()
        return max(odd[-1]-even[0],odd[0] - even[-1])
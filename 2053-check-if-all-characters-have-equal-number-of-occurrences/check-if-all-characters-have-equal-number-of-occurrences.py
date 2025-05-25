class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = defaultdict(int)
        for char in s:
            count[char] += 1
        curr = count[s[0]]
        for _,v in count.items():
            if curr != v:
                return False
        return True
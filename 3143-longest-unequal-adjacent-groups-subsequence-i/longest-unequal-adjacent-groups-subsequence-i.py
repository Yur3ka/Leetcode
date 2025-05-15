class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = []
        curr = 1 - groups[0]
        for i in range(len(words)):
            if groups[i] == curr:
                continue
            else:
                res.append( words[i])
                curr = 1 - curr
        return res
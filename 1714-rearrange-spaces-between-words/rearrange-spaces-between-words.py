class Solution:
    def reorderSpaces(self, text: str) -> str:
        space = text.count(' ')
        words = text.split()
        n = len(words)
        if n == 1:
            return words[0]+' '*space
        gap = space//(n-1)
        ans = []
        for w in words:
            ans.append(w)
            used = min(space,gap)
            ans.append(' '*used)
            space -= used
        ans.append(' '*space)
        return ''.join(ans)
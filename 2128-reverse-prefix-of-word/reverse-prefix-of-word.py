class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res = []
        flip = False
        for i in range(len(word)):
            res.append(word[i])
            if word[i] == ch and not flip:
                res.reverse()
                flip = True
        return ''.join(res)
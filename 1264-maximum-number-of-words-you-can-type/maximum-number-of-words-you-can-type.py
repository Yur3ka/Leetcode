class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0
        w_list = text.split()
        broken = set(list(brokenLetters))
        for word in w_list:
            if len(set(list(word))&broken) == 0:
                ans += 1

        return ans
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital_count = 0
        for char in word:
            if char.isupper():
                capital_count += 1
        if capital_count == 0 or capital_count == len(word):
            return True
        elif capital_count == 1 and word[0].isupper():
            return True
        return False
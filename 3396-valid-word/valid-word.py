class Solution:
    def isValid(self, word: str) -> bool:
        vowel = {'a','e','i','o','u'}
        number = {'1','2','3','4','5','6','7','8','9','0'}
        if len(word) < 3:
            return False
        v,c,n = 0,0,0
        for char in word:
            if char.lower() in vowel:
                v += 1
            elif char in number:
                n += 1
            elif char.isalpha():
                c += 1
            else:
                return False
        return c >= 1 and v >= 1
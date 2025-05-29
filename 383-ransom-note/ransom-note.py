class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = Counter(ransomNote)
        b = Counter(magazine)
        for key,val in a.items():
            if key not in b or val > b[key]:
                return False
        return True
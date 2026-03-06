class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        status = True
        for i in range(len(s)):
            if s[i] == '0':
                status = False
            if s[i] == '1' and status == False:
                return False
        return True
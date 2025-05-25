class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        w1 = []
        w2 = []
        
        for i in range(len(s)):
            if s[i] != goal[i]:
                w1.append(s[i])
                w2.append(goal[i])
        if len(w1) == 0:
            if len(set(s)) < len(s):
                return True
            else:
                return False
        elif len(w1) != 2:
            return False
        elif w1[0] != w2[1] or w1[1] != w2[0]:
            return False
        return True
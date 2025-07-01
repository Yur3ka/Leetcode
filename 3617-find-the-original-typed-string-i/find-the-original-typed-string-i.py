class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1
        current = 0
        s = 0
        for i in range(len(word)):
            if current == 0:
                current += 1
            else:
                if word[i] != word[i-1]:
                    if current != 1:
                        s+=1
                    ans += current -1
                    current = 1
                else:
                    current += 1
        if current != 0:
            ans += current-1
        # if s!= 0:
        #     ans -= 1
        return ans
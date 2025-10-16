class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = letters[0]
        s = 0 
        e = len(letters)-1
        while s <= e:
            m = (s+e)//2
            if letters[m]> target:
                ans = letters[m]
                e = m-1
            else:
                s = m+1
        return ans
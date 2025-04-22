class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        pos = {}
        ans = []
        for char in first_row:
            pos[char] = 1
        for char in second_row:
            pos[char] = 2
        for char in third_row:
            pos[char] = 3
        for word in words:
            curr = set()
            for char in word:
                curr.add(pos[char.lower()])
            if len(curr) == 1:
                ans.append(word)
        return ans
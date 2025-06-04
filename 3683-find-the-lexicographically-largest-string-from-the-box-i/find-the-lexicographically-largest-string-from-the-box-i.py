class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        if numFriends == 1:
            return word
        pos = defaultdict(list)
        max_char = 'a'
        for i in range(len(word)):
            pos[word[i]].append(i)
            max_char = max(max_char,word[i])
        res = ""
        for i in pos[max_char]:
            before = i
            after = max(numFriends - i - 1,0)
            res = max(res,word[i:n-after])
        return res

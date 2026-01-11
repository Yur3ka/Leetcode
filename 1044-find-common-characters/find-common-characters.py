class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = Counter(words[0])
        for i in range(1,len(words)):
            temp = {}
            new_counter = Counter(words[i])
            for k,v in new_counter.items():
                if k in ans:
                    temp[k] = min(ans[k], v)
            ans = temp
        res = []
        for k,v in ans.items():
            for _ in range(v):
                res.append(k)
        return res
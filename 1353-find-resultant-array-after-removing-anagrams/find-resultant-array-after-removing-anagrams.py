class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []
        for i in range(len(words)):
            if not ans:
                ans.append(words[i])
                bf = Counter(words[i])
            else:
                cr = Counter(words[i])
                
                if bf == cr:
                    continue
                else:
                    bf = cr
                    ans.append(words[i])
        # ans.append
        return ans
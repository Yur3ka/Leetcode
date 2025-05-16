class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        pre = [-1]*n
        dp = [1]*n
        max_in = 0
        def overlap(s1,s2):
            ans = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    ans += 1
            return ans
        len_dict = defaultdict(list)
        for i in range(n):
            len_dict[len(words[i])].append(i)
        ovl = [[-1]*n for _ in range(n)]
        for i in range(n-1):
            for j in range(i+1,n):
                if len(words[i]) == len(words[j]):
                    ovl[i][j] = overlap(words[i], words[j])
        for i in range(n):
            for num in len_dict[len(words[i])]:
                if num == i:
                    break
                if (groups[num] != groups[i]) and (ovl[num][i]) == 1:
                    curr = dp[num] + 1
                    if curr > dp[i]:
                        dp[i] = curr
                        pre[i] = num
                        if curr >= dp[max_in]:
                            max_in = i
        res = []
        while max_in != -1:
            res.append(words[max_in])
            max_in = pre[max_in]
        res.reverse()
        return res


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        ans = []
        def extract(s):
            low = []
            no_v = []
            for char in s:
                low.append(char.lower())
                if char.lower() not in ['a','e','i','o','u']:
                    no_v.append(char.lower())
                else:
                    no_v.append('*')
            L = ''.join(low)
            N = ''.join(no_v)
            return L,N
        w_list = defaultdict(list)
        for w in wordlist:
            L,N = extract(w)
            w_list[L].append(w)
            w_list[N].append(w)
            w_list[w].append(w)
        for w in queries:
            L,N = extract(w)
            if w in set(wordlist):
                ans.append(w)
            elif L in w_list:
                ans.append(w_list[L][0])
            elif N in w_list:
                ans.append(w_list[N][0])
            else:
                ans.append('')
        return ans
